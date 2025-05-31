"""
Renderer module for CTchargen.

This module handles rendering character data to different formats.
"""

import os
import string
from typing import Dict, List, Any, Optional, Union

import glob
from src.config import config


class TemplateRenderer:
    """
    Class for rendering character data using templates.
    """
    
    def __init__(self, template_name: str = None):
        """
        Initialize the renderer with a template.
        
        Args:
            template_name: Name of the template to use (without extension)
        """
        if template_name is None:
            template_name = config.get('default_template', 'text')
        
        self.template_name = template_name
        self.template_path = config.get_template_path(template_name)
        self.template_content = self._load_template()
    
    def _load_template(self) -> str:
        """
        Load the template content from file.
        
        Returns:
            str: Template content
        """
        try:
            with open(self.template_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Template file not found: {self.template_path}")
            print("Using default template.")
            return "{name}\nUPP: {upp_string}\nSkills: {skills_string}"
    
    def render(self, character_data: Dict[str, Any]) -> str:
        """
        Render character data using the template.
        
        Args:
            character_data: Dictionary of character data
            
        Returns:
            str: Rendered character data
        """
        # Use string.Template for simple template substitution
        template_content = self.template_content
        
        # Prepare the data for rendering
        render_data = {}
        for key, value in character_data.items():
            if isinstance(value, dict):
                # Flatten nested dictionaries
                for subkey, subvalue in value.items():
                    render_data[f"{key}_{subkey}"] = subvalue
            elif isinstance(value, list):
                # Join lists with commas
                render_data[key] = ", ".join(value) if value else "None"
            else:
                render_data[key] = value
        
        # Add rank title if available
        if 'career' in character_data and 'rank' in character_data:
            from src.careers import CAREERS
            career = character_data['career']
            rank_index = character_data['rank']
            
            if career in CAREERS and rank_index < len(CAREERS[career]['ranks']):
                rank_title = CAREERS[career]['ranks'][rank_index]
                render_data['rank'] = f"{rank_title} (Rank {rank_index})"
        
        # Handle special template variables
        
        # Status (died)
        if 'died' in character_data:
            died = character_data['died']
            status = "Deceased (died during service)" if died else "Active"
            template_content = template_content.replace("${died ? \"Deceased (died during service)\" : \"Active\"}", status)
        
        # Psionics
        if 'psionic' in character_data:
            psionic = character_data['psionic']
            psionic_text = "None"
            
            if psionic.get('has_psionic', False):
                psr = psionic.get('psr', 0)
                is_trained = psionic.get('is_trained', False)
                talents = psionic.get('talents', [])
                
                if is_trained:
                    talents_str = ", ".join(talents) if talents else "None"
                    if "**PSR:**" in template_content:  # Markdown format
                        psionic_text = f"**PSR:** {psr} (Trained)  \n**Talents:** {talents_str}"
                    else:  # Text format
                        psionic_text = f"PSR {psr} (Trained) - Talents: {talents_str}"
                else:
                    if "**PSR:**" in template_content:  # Markdown format
                        psionic_text = f"**PSR:** {psr} (Untrained)"
                    else:  # Text format
                        psionic_text = f"PSR {psr} (Untrained)"
            
            template_content = template_content.replace(
                "${psionic.has_psionic ? (psionic.is_trained ? `**PSR:** ${psionic.psr} (Trained)  \\n**Talents:** ${psionic.talents.length ? psionic.talents.join(\", \") : \"None\"}` : `**PSR:** ${psionic.psr} (Untrained)`) : \"None\"}",
                psionic_text
            )
            
            template_content = template_content.replace(
                "${psionic.has_psionic ? (psionic.is_trained ? `PSR ${psionic.psr} (Trained) - Talents: ${psionic.talents.length ? psionic.talents.join(\", \") : \"None\"}` : `PSR ${psionic.psr} (Untrained)`) : \"None\"}",
                psionic_text
            )
        
        # Create a new template with the processed content
        template = string.Template(template_content)
        
        # Render the template
        try:
            return template.safe_substitute(render_data)
        except KeyError as e:
            print(f"Error rendering template: {e}")
            return str(character_data)
    
    def render_multiple(self, characters_data: List[Dict[str, Any]]) -> str:
        """
        Render multiple characters using the template.
        
        Args:
            characters_data: List of character data dictionaries
            
        Returns:
            str: Rendered characters data
        """
        rendered_characters = []
        for character_data in characters_data:
            rendered_characters.append(self.render(character_data))
        
        return "\n\n---\n\n".join(rendered_characters)
    
    def save(self, character_data: Dict[str, Any], filename: str, extension: Optional[str] = None) -> str:
        """
        Render character data and save to a file.
        
        Args:
            character_data: Dictionary of character data
            filename: Output filename
            extension: File extension (optional)
            
        Returns:
            str: Path to the saved file
        """
        rendered_data = self.render(character_data)
        output_path = config.get_output_path(filename, extension)
        
        try:
            with open(output_path, 'w') as f:
                f.write(rendered_data)
            return output_path
        except IOError as e:
            print(f"Error saving file: {e}")
            return ""
    
    def save_multiple(self, characters_data: List[Dict[str, Any]], filename: str, extension: Optional[str] = None) -> str:
        """
        Render multiple characters and save to a file.
        
        Args:
            characters_data: List of character data dictionaries
            filename: Output filename
            extension: File extension (optional)
            
        Returns:
            str: Path to the saved file
        """
        rendered_data = self.render_multiple(characters_data)
        output_path = config.get_output_path(filename, extension)
        
        try:
            with open(output_path, 'w') as f:
                f.write(rendered_data)
            return output_path
        except IOError as e:
            print(f"Error saving file: {e}")
            return ""


def render_character(character_data: Dict[str, Any], template_name: Optional[str] = None) -> str:
    """
    Render character data using a template.
    
    Args:
        character_data: Dictionary of character data
        template_name: Name of the template to use (optional)
        
    Returns:
        str: Rendered character data
    """
    renderer = TemplateRenderer(template_name)
    return renderer.render(character_data)


def save_character(character_data: Dict[str, Any], filename: str, 
                  template_name: Optional[str] = None, extension: Optional[str] = None) -> str:
    """
    Render character data and save to a file.
    
    Args:
        character_data: Dictionary of character data
        filename: Output filename
        template_name: Name of the template to use (optional)
        extension: File extension (optional)
        
    Returns:
        str: Path to the saved file
    """
    renderer = TemplateRenderer(template_name)
    return renderer.save(character_data, filename, extension)


def save_characters(characters_data: List[Dict[str, Any]], filename: str,
                   template_name: Optional[str] = None, extension: Optional[str] = None) -> str:
    """
    Render multiple characters and save to a file.
    
    Args:
        characters_data: List of character data dictionaries
        filename: Output filename
        template_name: Name of the template to use (optional)
        extension: File extension (optional)
        
    Returns:
        str: Path to the saved file
    """
    renderer = TemplateRenderer(template_name)
    return renderer.save_multiple(characters_data, filename, extension)


def get_available_templates() -> List[str]:
    """
    Get a list of available templates.
    
    Returns:
        List[str]: List of template names (without extension)
    """
    templates_dir = config.TEMPLATES_DIR
    template_files = glob.glob(os.path.join(templates_dir, "*.template"))
    
    # Extract template names without extension
    template_names = [os.path.splitext(os.path.basename(f))[0] for f in template_files]
    
    return template_names
