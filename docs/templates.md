# Template System Documentation

The CTchargen template system allows for flexible output formatting of character data. This document explains how to use and create templates.

## Overview

Templates are text files with placeholders that get replaced with character data when rendering. The system uses Python's `string.Template` for simple string substitution.

## Available Templates

The following templates are included with CTchargen:

- `text.template`: Plain text format for character sheets
- `markdown.template`: Markdown format for character sheets
- `death.template`: List of characters who have died during character generation
- `world.template`: World generation format
- `names.template`: Name generation format
- `sector_grid.html`: HTML format for sector grids

## Template Placeholders

Templates use the `${variable_name}` syntax for placeholders. The following placeholders are available:

### Basic Character Information
- `${name}`: Character name
- `${upp_string}`: Universal Personality Profile as a string
- `${gender}`: Character gender
- `${race}`: Character race
- `${age}`: Character age

### Career Information
- `${career}`: Character career
- `${rank}`: Character rank
- `${terms}`: Number of terms served

### Skills and Abilities
- `${skills_string}`: Formatted list of character skills

### Equipment
- `${weapons}`: Character weapons
- `${armor}`: Character armor
- `${equipment}`: Other equipment
- `${cash}`: Character's cash amount

## Creating Custom Templates

You can create your own templates by adding a file to the `templates/` directory with a `.template` extension. 

### Example Template

Here's a simple example template:

```
# ${name}

## Basic Information
- UPP: ${upp_string}
- Gender: ${gender}
- Race: ${race}
- Age: ${age}

## Career
- Career: ${career}
- Rank: ${rank}
- Terms: ${terms}

## Skills
${skills_string}

## Equipment
Weapons: ${weapons}
Armor: ${armor}
Other: ${equipment}
Cash: Cr${cash}
```

### Using Custom Templates

To use a custom template, specify the template name (without the `.template` extension) when generating characters:

```
python chargen.py -t my_custom_template
```

Or when using the API:

```python
from src.renderer import save_characters

save_characters(characters_data, "output_filename", "my_custom_template")
```

## Advanced Template Features

### Nested Data

For nested data structures, the renderer flattens the structure using underscores. For example, if a character has a `stats` dictionary with a `strength` key, you can access it in the template as `${stats_strength}`.

### Lists

Lists are automatically joined with commas. For example, if a character has a `skills` list, it will be rendered as a comma-separated string.

### Conditional Content

The template system does not directly support conditional content. However, you can create multiple templates for different scenarios and choose the appropriate one based on your needs.

## Troubleshooting

If a placeholder in your template doesn't have a corresponding value in the character data, it will be left as is in the output. To avoid this, ensure that all placeholders in your template have corresponding values in the character data.
