# Character Generation Documentation

This document explains how the CTchargen character generation system works and how to use it.

## Overview

CTchargen generates random characters for the Classic Traveller role-playing game. Characters have characteristics, skills, and equipment, and can be output in various formats using customizable templates.

## Character Generation Process

The character generation process follows these steps:

1. Generate basic characteristics (UPP - Universal Personality Profile)
2. Determine gender and race
3. Generate a name
4. Determine career and rank
5. Generate skills
6. Assign equipment and cash

## Using the Character Generator

### Command Line Interface

The simplest way to generate characters is using the command line interface:

```
python chargen.py [options]
```

Options:
- `-n, --num-characters`: Number of characters to generate (default: 1)
- `-o, --output`: Output filename without extension (default: "characters")
- `-t, --template`: Template to use (default: "text")
- `-f, --format`: Output file format (default: "txt")
- `-c, --config`: Path to configuration file
- `-v, --verbose`: Enable verbose output

Example:
```
python chargen.py -n 5 -o my_characters -t text -f txt -v
```

### Helper Scripts

For convenience, you can use the provided helper scripts:

- `generate_characters.py`: Python script for generating characters
- `generate.bat`: Windows batch file for generating characters
- `generate.sh`: Unix shell script for generating characters

Example:
```
python generate_characters.py -n 3 -t markdown -f md -o output/markdown_characters
```

### Python API

You can also use the Python API to generate characters programmatically:

```python
from src.character import generate_characters
from src.renderer import save_characters

# Generate 3 characters
characters = generate_characters(3)

# Convert to dictionaries
characters_data = [character.to_dict() for character in characters]

# Save to file using the text template
output_path = save_characters(characters_data, "my_characters", "text", "txt")
print(f"Characters saved to: {output_path}")
```

## Character Data Structure

Each character has the following attributes:

### Basic Characteristics

- `name`: Character name
- `upp`: Universal Personality Profile (list of integers)
- `upp_string`: UPP as a string
- `gender`: Character gender
- `race`: Character race
- `age`: Character age

### Career Information

- `career`: Character career
- `rank`: Character rank
- `terms`: Number of terms served

### Skills and Abilities

- `skills`: Dictionary of skills and their levels
- `skills_string`: Formatted list of character skills

### Equipment

- `weapons`: Character weapons
- `armor`: Character armor
- `equipment`: Other equipment
- `cash`: Character's cash amount

## Customizing Character Generation

You can customize the character generation process by modifying the configuration. See the [Configuration Documentation](configuration.md) for details.

### Custom Races

You can add custom races by adding them to the `races` list in the configuration:

```json
{
  "races": [
    "Human", "Elf", "Dwarf", "Halfling", "Gnome"
  ]
}
```

### Custom Weapons and Equipment

You can add custom weapons and equipment by adding them to the `guns`, `melee`, and `vehicles` lists in the configuration:

```json
{
  "guns": [
    "Laser Pistol", "Plasma Rifle", "Gauss Gun", "Needler"
  ],
  "melee": [
    "Vibroblade", "Power Sword", "Force Axe", "Neural Whip"
  ]
}
```

## Advanced Usage

### Generating Multiple Characters

To generate multiple characters, use the `-n` option:

```
python chargen.py -n 10
```

Or programmatically:

```python
from src.character import generate_characters

characters = generate_characters(10)
```

### Custom Output Formats

You can create custom output formats by creating new templates. See the [Template Documentation](templates.md) for details.

### Extending the Character Class

You can extend the `Character` class to add custom functionality:

```python
from src.character import Character

class CustomCharacter(Character):
    def __init__(self):
        super().__init__()
        self.custom_attribute = "Custom Value"
    
    def custom_method(self):
        return f"Custom method for {self.name}"
```

## Troubleshooting

If you encounter issues with character generation:

1. Check the configuration to ensure it's valid
2. Verify that the templates are correctly formatted
3. Ensure that the output directory exists and is writable
4. Check the console output for error messages
