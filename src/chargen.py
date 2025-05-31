"""
Main module for CTchargen.

This module provides the main entry point for the character generator.
"""

import os
import sys
import argparse
from typing import List, Dict, Any, Optional

from src.character import Character, generate_characters
from src.renderer import save_character, save_characters
from src.config import config


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Classic Traveller Character Generator",
        epilog="Example: chargen.py -n 5 -o characters -t text"
    )
    
    parser.add_argument(
        "-n", "--num-characters",
        type=int,
        default=config.get('default_num_characters', 1),
        help="Number of characters to generate (default: 1)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="characters",
        help="Output filename (without extension)"
    )
    
    parser.add_argument(
        "-t", "--template",
        type=str,
        default=config.get('default_template', 'text'),
        help="Template to use for output (default: text)"
    )
    
    parser.add_argument(
        "-f", "--format",
        type=str,
        default=config.get('default_output_format', 'txt'),
        help="Output file format (default: txt)"
    )
    
    parser.add_argument(
        "-c", "--config",
        type=str,
        help="Path to configuration file"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    return parser.parse_args()


def generate_and_save_characters(num_characters: int, output_filename: str, 
                                template_name: str, output_format: str, 
                                verbose: bool = False) -> str:
    """
    Generate characters and save them to a file.
    
    Args:
        num_characters: Number of characters to generate
        output_filename: Output filename (without extension)
        template_name: Template to use for output
        output_format: Output file format
        verbose: Enable verbose output
        
    Returns:
        str: Path to the saved file
    """
    if verbose:
        print(f"Generating {num_characters} characters...")
    
    # Generate characters
    characters = generate_characters(num_characters)
    
    # Convert characters to dictionaries
    characters_data = [character.to_dict() for character in characters]
    
    if verbose:
        print(f"Saving characters to {output_filename}.{output_format}...")
    
    # Save characters to file
    output_path = save_characters(
        characters_data, 
        output_filename, 
        template_name, 
        output_format
    )
    
    if verbose:
        print(f"Characters saved to {output_path}")
    
    return output_path


def main() -> None:
    """Main entry point for the character generator."""
    # Parse command line arguments
    args = parse_args()
    
    # Generate and save characters
    output_path = generate_and_save_characters(
        args.num_characters,
        args.output,
        args.template,
        args.format,
        args.verbose
    )
    
    # Print the output path
    print(f"Characters saved to: {output_path}")


if __name__ == "__main__":
    main()
