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
        print(f"Gender: {characters[0].gender}")
        print(f"Race: {characters[0].race}")
        print(f"Age: {characters[0].age}")
        print(f"Career: {characters[0].career}")
        
        rank_title = characters[0].get_rank_title()
        rank_display = f"{rank_title} (Rank {characters[0].rank})" if rank_title else f"Rank {characters[0].rank}"
        print(f"Rank: {rank_display}")
        
        print(f"Terms: {characters[0].terms}")
        
        status = "Deceased (died during service)" if characters[0].died else "Active"
        print(f"Status: {status}")
        
        print(f"Skills: {characters[0].get_skills_string()}")
        
        weapons_str = ", ".join(characters[0].weapons) if characters[0].weapons else "None"
        print(f"Weapons: {weapons_str}")
        
        print(f"Armor: {characters[0].armor or 'None'}")
        
        equipment_str = ", ".join(characters[0].equipment) if characters[0].equipment else "None"
        print(f"Equipment: {equipment_str}")
        
        print(f"Cash: {characters[0].cash} Credits")
        
        print(f"Psionics: {characters[0].get_psionic_string()}")


if __name__ == "__main__":
    main()
