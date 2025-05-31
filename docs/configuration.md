# Configuration System Documentation

The CTchargen configuration system allows for customizing various aspects of the character generation process. This document explains how to configure the generator.

## Overview

CTchargen uses a configuration system that allows you to customize various aspects of the character generation process. The configuration is loaded from a JSON file or can be set programmatically.

## Default Configuration

The default configuration includes:

```json
{
  "output_dir": "output/",
  "default_template": "text",
  "default_output_format": "txt",
  "default_num_characters": 1,
  "name_generation": {
    "use_phonetic": true,
    "data_file": "data/syllable_starter.json"
  },
  "races": [
    "Aslan", "Droyne", "Hiver", "Humaniti", "K'kree", "Vargr",
    "Solomani", "Vilani", "Zhodani", "Imperial", "Darrian",
    "Geonee", "Suerrat"
  ],
  "guns": [
    "Body Pistol", "Autopistol", "Revolver", "Carbine", "Rifle",
    "Autorifle", "Shotgun", "SMG", "Laser Carbine", "Laser Rifle"
  ],
  "melee": [
    "Blade", "Foil", "Cutlass", "Sword", "Broadsword", "Bayonet",
    "Spear", "Halberd", "Pike", "Cudgel"
  ],
  "vehicles": [
    "Aircraft (Helicopter)", "Aircraft (Propeller-driven)",
    "Aircraft (Jet-driven)", "Grav Vehicle", "Tracked Vehicle",
    "Wheeled Vehicle", "Watercraft (Small Watercraft)",
    "Watercraft (Large Watercraft)", "Watercraft (Hovercraft)",
    "Watercraft (Submerisible)"
  ]
}
```

## Configuration Options

### General Options

- `output_dir`: Directory where output files will be saved
- `default_template`: Default template to use for rendering
- `default_output_format`: Default file format for output files
- `default_num_characters`: Default number of characters to generate

### Name Generation Options

- `name_generation.use_phonetic`: Whether to use phonetic name generation
- `name_generation.data_file`: Path to the syllable data file

### Character Options

- `races`: List of available races
- `guns`: List of available guns
- `melee`: List of available melee weapons
- `vehicles`: List of available vehicles

## Using a Custom Configuration File

You can specify a custom configuration file when running the generator:

```
python chargen.py -c my_config.json
```

Or when using the API:

```python
from src.config import Config

config = Config("my_config.json")
```

## Creating a Custom Configuration File

To create a custom configuration file, create a JSON file with your desired settings. You only need to include the settings you want to override; any settings not specified will use the default values.

Example custom configuration:

```json
{
  "output_dir": "my_output",
  "default_template": "markdown",
  "default_output_format": "md",
  "default_num_characters": 3,
  "name_generation": {
    "use_phonetic": true
  },
  "races": [
    "Human", "Elf", "Dwarf", "Halfling", "Gnome"
  ]
}
```

## Programmatic Configuration

You can also configure the generator programmatically:

```python
from src.config import config

# Override configuration settings
config.config['output_dir'] = 'my_output'
config.config['default_template'] = 'markdown'
config.config['default_output_format'] = 'md'
config.config['default_num_characters'] = 3

# Use the configuration
from src.character import generate_characters
characters = generate_characters(config.config['default_num_characters'])
```

## Configuration Paths

The configuration system uses several paths for locating files:

- `BASE_DIR`: The base directory of the project
- `SRC_DIR`: The source code directory
- `DATA_DIR`: The data directory
- `TEMPLATES_DIR`: The templates directory
- `NAMES_DIR`: The names directory
- `OUTPUT_DIR`: The output directory

These paths are used by the generator to locate files. You can access them through the `Config` class:

```python
from src.config import Config

config = Config()
print(f"Base directory: {Config.BASE_DIR}")
print(f"Templates directory: {Config.TEMPLATES_DIR}")
```

## Troubleshooting

If you're having issues with the configuration:

1. Ensure your JSON file is valid
2. Check that the paths in your configuration are correct
3. Verify that the directories specified in your configuration exist
4. Make sure the configuration file is in the correct location
