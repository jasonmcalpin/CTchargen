"""
Test script for character generation.
"""

import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.character import generate_character

def main():
    """Generate and print a test character."""
    character = generate_character()
    print(character)

if __name__ == "__main__":
    main()
