# CTchargen - Classic Traveller Character Generator

A character generator for the Classic Traveller RPG system.

## Overview

CTchargen is a Python-based character generator for the Classic Traveller role-playing game. It creates random characters with characteristics, skills, and equipment, and can output them in various formats using customizable templates.

## Features

- Generate random Classic Traveller characters with:
  - Hexadecimal UPP values (e.g., "7A8B9C")
  - Authentic career generation with proper enlistment, survival, commission, promotion, and re-enlistment rolls
  - Skills based on career and terms served
  - Weapons, armor, and equipment appropriate to career
  - Cash based on career and terms served
  - Psionic abilities with PSR generation, training checks, and talent selection
  - Aging effects for characters with multiple terms
  - Character death during service (failed survival roll)
- Customizable character traits and equipment
- Multiple output formats using templates (text, markdown)
- Command-line interface for easy use
- Web interface for browser-based access
- RESTful API for integration with other tools
- Configurable settings

## Installation

### Prerequisites

- Python 3.6 or higher
- Node.js 14 or higher (for web interface)

### Automated Installation

Use the provided installation script to set up the project:

```
python install.py
```

This will:
1. Create a virtual environment
2. Install Python dependencies
3. Set up the frontend
4. Create necessary directories

### Manual Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/CTchargen.git
   cd CTchargen
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

4. Install backend dependencies:
   ```
   pip install -r web/backend/requirements.txt
   ```

5. Install frontend dependencies:
   ```
   cd web/frontend
   npm install
   ```

## Usage

### Web Interface

The web interface provides a user-friendly way to generate and view characters.

#### All-in-One Startup

Use the all-in-one startup script to start both the backend and frontend servers and open the web interface in your browser:

- Windows: `start.bat`
- Unix/MacOS: `./start.sh`

#### Troubleshooting Frontend Build Issues

If you encounter issues when building the frontend, use the provided fix script:

- Windows: `fix_frontend_build.bat`
- Unix/MacOS: `./fix_frontend_build.sh`

This script will:
1. Install any missing dependencies
2. Update TypeScript configuration to be less strict
3. Install necessary type definitions
4. Attempt to build the frontend

#### Manual Startup

If you prefer to start the servers manually:

1. Start the backend server:
   - Windows: `run_backend.bat`
   - Unix/MacOS: `./run_backend.sh`

2. Start the frontend development server:
   - Windows: `run_frontend.bat`
   - Unix/MacOS: `./run_frontend.sh`

3. Open your browser and navigate to `http://localhost:3000`

### Command Line Interface

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

### As a Python Module

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

### RESTful API

The project includes a RESTful API that can be used to generate characters programmatically.

API Endpoints:
- `GET /api/characters/templates` - List available templates
- `GET /api/characters/config` - Get current configuration
- `POST /api/characters/generate` - Generate characters

Example API request:
```
curl -X POST http://localhost:8000/api/characters/generate \
  -H "Content-Type: application/json" \
  -d '{"num_characters": 3, "template": "text", "output_format": "txt"}'
```

## Configuration

The generator can be configured using a JSON configuration file. Create a file named `config.json` in the project directory with your custom settings.

Example configuration:
```json
{
  "output_dir": "output",
  "default_template": "text",
  "default_output_format": "txt",
  "default_num_characters": 1,
  "name_generation": {
    "use_phonetic": true
  }
}
```

## Templates

The generator uses template files to format the output. Template files are located in the `templates/` directory and use a simple string substitution format.

Available templates:
- `text.template`: Plain text format
- `markdown.template`: Markdown format
- `death.template`: Death & Dismemberment format
- `world.template`: World generation format

Both the text and markdown templates now include:
- Career information (career, rank, terms served)
- Character status (active or deceased)
- Psionic information (PSR, training status, talents)

### Custom Templates

You can create your own templates by adding a file to the `templates/` directory. Template files use Python's string.Template format with placeholders for character attributes.

Example template:
```
Name: ${name}
UPP: ${upp_string}
Gender: ${gender}
Race: ${race}
Age: ${age}
Career: ${career}
Rank: ${rank}
Terms: ${terms}
Skills: ${skills_string}
Weapons: ${weapons}
Armor: ${armor}
Equipment: ${equipment}
Cash: ${cash} Credits
```


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

- Original concept by Omer Golan-Joel
- Significant development and enhancements by Jason McAlpin, including:
  - World generation system
  - Word generation system
  - Template system
  - Command-line interface
- Web interface and API by Jason McAlpin
- Currently maintained by Jason McAlpin
