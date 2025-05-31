# Changelog

All notable changes to the CTchargen project will be documented in this file.

## [3.2.0] - 2025-05-30

### Added
- Classic Traveller career generation with proper enlistment, survival, commission, promotion, and re-enlistment rolls
- Psionic system with PSR generation, training checks, and talent selection
- Character death during service (failed survival roll)
- Aging effects for characters with multiple terms
- Updated templates to display psionic information and character status
- New documentation for the psionic system

### Changed
- Career generation now uses authentic Classic Traveller tables and rules
- Character terms are now determined by re-enlistment rolls rather than random assignment
- Character generation is now more faithful to the Classic Traveller rulebook

## [3.1.0] - 2025-05-30

### Added
- Career generation system with six career paths (Navy, Marines, Army, Scouts, Merchants, Other)
- Rank generation based on career and terms served
- Skill acquisition based on career and terms served
- Equipment generation (weapons, armor, and gear) appropriate to career
- Cash generation based on career and terms served
- Hexadecimal UPP values (e.g., "7A8B9C" instead of "771011106")
- Updated templates to display career, rank, terms, skills, weapons, armor, equipment, and cash
- Improved character preview in command-line output

### Changed
- Character generation now includes complete career information
- Templates updated to support new character attributes
- Renderer updated to handle rank titles in templates

## [3.0.0] - 2025-05-30

### Major Changes
- Complete project restructuring into a proper Python package
- Added proper directory organization for outputs, templates, data, and names
- Improved code organization with proper typing annotations and docstrings
- Enhanced error handling throughout the codebase
- Fixed path handling issues for output files

### Added
- New Markdown template for better formatted output
- Helper scripts for common operations (generate_characters.py, generate.bat, generate.sh)
- Installation script for development mode (install.py)
- Requirements.txt for dependencies
- MIT License file
- Comprehensive .gitignore file
- Enhanced README with better documentation

### Changed
- All output files now go to the output/ directory
- Improved configuration management
- Updated credits to properly reflect contributions

## [2.0.0] - Previous Version

### Added
- Template system for flexible output formats
- Command-line interface for easy use
- World generation system
- Word generation system based on phonetic rules

## [1.0.0] - Original Release

### Added
- Initial character generation for Classic Traveller
- Basic character traits and equipment generation
