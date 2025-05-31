"""
Helper functions for the CTchargen web interface.
"""
import os
import sys
from typing import List, Dict, Any, Optional
import json


def get_project_root() -> str:
    """Get the absolute path to the project root directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))


def ensure_output_dir(output_dir: str = "output") -> str:
    """
    Ensure that the output directory exists.
    
    Args:
        output_dir: The output directory path (relative to project root)
        
    Returns:
        The absolute path to the output directory
    """
    project_root = get_project_root()
    output_path = os.path.join(project_root, output_dir)
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    return output_path


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename to ensure it's safe to use.
    
    Args:
        filename: The filename to sanitize
        
    Returns:
        A sanitized filename
    """
    # Replace potentially dangerous characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
        
    # Ensure the filename is not empty
    if not filename:
        filename = "output"
        
    return filename


def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Load a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        The loaded JSON data as a dictionary
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Error loading JSON file {file_path}: {str(e)}")


def save_json_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to a JSON file.
    
    Args:
        data: The data to save
        file_path: Path to the JSON file
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        raise ValueError(f"Error saving JSON file {file_path}: {str(e)}")
