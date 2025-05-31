"""
API endpoints for character generation.
"""
import os
import sys
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query

# Add the project root to the Python path to import the CTchargen modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

# Import CTchargen modules
try:
    from src.character import generate_characters as generate_chars
    from src.renderer import save_characters, get_available_templates
    from src.config import Config
except ImportError:
    # Fallback to the old module structure if src/ is not available
    from lib.stellagama import random_choice
    # We'll implement a simplified version later if needed

from web.backend.models.character import (
    CharacterGenerationRequest,
    CharacterGenerationResponse,
    Character,
    TemplateListResponse,
    ConfigurationResponse,
)

# Create router
router = APIRouter(prefix="/api/characters", tags=["characters"])


@router.post("/generate", response_model=CharacterGenerationResponse)
async def generate_characters(request: CharacterGenerationRequest):
    """Generate characters based on the request parameters."""
    try:
        # Generate characters
        characters = generate_chars(request.num_characters)
        
        # Convert to dictionaries
        character_dicts = [character.to_dict() for character in characters]
        
        # Save to file if output_filename is provided
        output_path = None
        if request.output_filename:
            output_path = save_characters(
                character_dicts,
                request.output_filename,
                request.template,
                request.output_format
            )
        
        # Convert to response model
        character_models = []
        for char_dict in character_dicts:
            character_models.append(Character(
                name=char_dict.get("name", ""),
                upp=char_dict.get("upp", []),
                upp_string=char_dict.get("upp_string", ""),
                gender=char_dict.get("gender", ""),
                race=char_dict.get("race", ""),
                age=char_dict.get("age", 0),
                career=char_dict.get("career", ""),
                rank=char_dict.get("rank", ""),
                terms=char_dict.get("terms", 0),
                skills=char_dict.get("skills", {}),
                skills_string=char_dict.get("skills_string", ""),
                weapons=char_dict.get("weapons", ""),
                armor=char_dict.get("armor", ""),
                equipment=char_dict.get("equipment", ""),
                cash=char_dict.get("cash", 0)
            ))
        
        return CharacterGenerationResponse(
            characters=character_models,
            output_path=output_path,
            template_used=request.template,
            format_used=request.output_format
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating characters: {str(e)}")


@router.get("/templates", response_model=TemplateListResponse)
async def list_templates():
    """List available templates."""
    try:
        templates = get_available_templates()
        config = Config()
        default_template = config.config.get("default_template", "text")
        
        return TemplateListResponse(
            templates=templates,
            default_template=default_template
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing templates: {str(e)}")


@router.get("/config", response_model=ConfigurationResponse)
async def get_config():
    """Get the current configuration."""
    try:
        config = Config()
        return ConfigurationResponse(config=config.config)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting configuration: {str(e)}")
