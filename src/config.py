"""
Configuration module for CTchargen.

This module handles configuration settings for the character generator.
"""

import os
import json
from typing import Dict, Any, List, Optional

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, 'src')
DATA_DIR = os.path.join(BASE_DIR, 'data')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
NAMES_DIR = os.path.join(BASE_DIR, 'names')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# Default configuration
DEFAULT_CONFIG = {
    'output_dir': OUTPUT_DIR,
    'default_template': 'text',
    'default_output_format': 'txt',
    'default_num_characters': 1,
    'name_generation': {
        'use_phonetic': True,
        'data_file': os.path.join(DATA_DIR, 'syllable_starter.json'),
    },
    'races': [
        "Aslan", "Droyne", "Hiver", "Humaniti", "K'kree", "Vargr",
        "Solomani", "Vilani", "Zhodani", "Imperial", "Darrian",
        "Geonee", "Suerrat"
    ],
    'guns': [
        "Body Pistol", "Autopistol", "Revolver", "Carbine", "Rifle",
        "Autorifle", "Shotgun", "SMG", "Laser Carbine", "Laser Rifle"
    ],
    'melee': [
        "Blade", "Foil", "Cutlass", "Sword", "Broadsword", "Bayonet",
        "Spear", "Halberd", "Pike", "Cudgel"
    ],
    'vehicles': [
        "Aircraft (Helicopter)", "Aircraft (Propeller-driven)",
        "Aircraft (Jet-driven)", "Grav Vehicle", "Tracked Vehicle",
        "Wheeled Vehicle", "Watercraft (Small Watercraft)",
        "Watercraft (Large Watercraft)", "Watercraft (Hovercraft)",
        "Watercraft (Submerisible)"
    ]
}


class Config:
    """
    Configuration class for CTchargen.
    
    This class handles loading and accessing configuration settings.
    """
    
    # Class-level constants
    BASE_DIR = BASE_DIR
    SRC_DIR = SRC_DIR
    DATA_DIR = DATA_DIR
    TEMPLATES_DIR = TEMPLATES_DIR
    NAMES_DIR = NAMES_DIR
    OUTPUT_DIR = OUTPUT_DIR
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the configuration.
        
        Args:
            config_file: Path to a JSON configuration file (optional)
        """
        self.config = DEFAULT_CONFIG.copy()
        
        if config_file and os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading configuration file: {e}")
                print("Using default configuration.")
        
        # Ensure output directory exists
        os.makedirs(self.config['output_dir'], exist_ok=True)
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key is not found
            
        Returns:
            The configuration value
        """
        return self.config.get(key, default)
    
    def get_template_path(self, template_name: str) -> str:
        """
        Get the full path to a template file.
        
        Args:
            template_name: Name of the template without extension
            
        Returns:
            Full path to the template file
        """
        return os.path.join(TEMPLATES_DIR, f"{template_name}.template")
    
    def get_output_path(self, filename: str, extension: Optional[str] = None) -> str:
        """
        Get the full path to an output file.
        
        Args:
            filename: Base filename
            extension: File extension (optional, uses default if not provided)
            
        Returns:
            Full path to the output file
        """
        if extension is None:
            extension = self.config['default_output_format']
        
        # Remove any existing extension
        if '.' in filename:
            filename = filename.split('.')[0]
        
        # Handle paths with directory separators
        if '/' in filename or '\\' in filename:
            # Extract just the filename part
            base_filename = os.path.basename(filename)
            return os.path.join(self.config['output_dir'], f"{base_filename}.{extension}")
        else:
            return os.path.join(self.config['output_dir'], f"{filename}.{extension}")
    
    def get_races(self) -> List[str]:
        """
        Get the list of available races.
        
        Returns:
            List of race names
        """
        return self.config['races']
    
    def get_guns(self) -> List[str]:
        """
        Get the list of available guns.
        
        Returns:
            List of gun names
        """
        return self.config['guns']
    
    def get_melee(self) -> List[str]:
        """
        Get the list of available melee weapons.
        
        Returns:
            List of melee weapon names
        """
        return self.config['melee']
    
    def get_vehicles(self) -> List[str]:
        """
        Get the list of available vehicles.
        
        Returns:
            List of vehicle names
        """
        return self.config['vehicles']


# Create a singleton instance
config = Config()
