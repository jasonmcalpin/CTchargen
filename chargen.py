#!/usr/bin/env python3
"""
Classic Traveller Character Generator

This script is the main entry point for the character generator.
"""

import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main module
from src.chargen import main

if __name__ == "__main__":
    main()
