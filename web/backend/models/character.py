"""
Pydantic models for character generation.
"""
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


class CharacterGenerationRequest(BaseModel):
    """Request model for character generation."""
    num_characters: int = Field(1, description="Number of characters to generate", ge=1, le=100)
    template: str = Field("text", description="Template to use for output")
    output_format: str = Field("txt", description="Output file format")
    output_filename: Optional[str] = Field(None, description="Output filename without extension")
    config_path: Optional[str] = Field(None, description="Path to configuration file")


class CharacterSkill(BaseModel):
    """Model for a character skill."""
    name: str
    level: int


class Character(BaseModel):
    """Model for a character."""
    name: str
    upp: Dict[str, int]
    upp_string: str
    gender: str
    race: str
    age: int
    career: str
    rank: int
    terms: int
    skills: Dict[str, int]
    skills_string: str
    weapons: List[str]
    armor: str
    equipment: List[str]
    cash: int


class CharacterGenerationResponse(BaseModel):
    """Response model for character generation."""
    characters: List[Character]
    output_path: Optional[str] = None
    template_used: str
    format_used: str


class TemplateListResponse(BaseModel):
    """Response model for template listing."""
    templates: List[str]
    default_template: str


class ConfigurationResponse(BaseModel):
    """Response model for configuration."""
    config: Dict[str, Any]
