#!/usr/bin/env python
"""
Character generation script for CTchargen.

This script provides a simple interface to generate characters with common options.
"""

import argparse
import os
import sys

from src.character import generate_characters
from src.renderer import save_characters


def main():
    """Generate characters with common options."""
    parser = argparse.ArgumentParser(description="Generate Classic Traveller characters")
    parser.add_argument("-n", "--num", type=int, default=1, help="Number of characters to generate")
    parser.add_argument("-o", "--output", default="characters", help="Output filename")
    parser.add_argument(
        "-t", "--template", default="text", choices=["text", "markdown"], 
        help="Template to use"
    )
    parser.add_argument(
        "-f", "--format", default="txt", choices=["txt", "md"], 
        help="Output file format"
    )
    args = parser.parse_args()

    print(f"Generating {args.num} characters...")
    characters = generate_characters(args.num)
    characters_data = [character.to_dict() for character in characters]
    
    output_path = save_characters(
        characters_data, args.output, args.template, args.format
    )
    
    print(f"Characters saved to: {output_path}")
    
    # Print a preview of the first character
    if characters:
        print("\nPreview of first character:")
        print(f"Name: {characters[0].name}")
        print(f"UPP: {characters[0].get_upp_string()}")
        print(f"Career: {characters[0].career}")
        print(f"Skills: {characters[0].get_skills_string()}")


if __name__ == "__main__":
    main()
