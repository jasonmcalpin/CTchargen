# Contributing to CTchargen

Thank you for considering contributing to CTchargen! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project. We aim to foster an inclusive and welcoming community.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes
4. Run tests to ensure your changes don't break existing functionality
5. Submit a pull request

## Development Setup

1. Clone the repository:
   ```
   git clone https://github.com/golan2072/CTchargen.git
   cd CTchargen
   ```

2. Install the package in development mode:
   ```
   python install.py
   ```
   
   Or manually:
   ```
   pip install -e .
   ```

## Coding Standards

- Follow PEP 8 style guidelines
- Add type hints to all functions and methods
- Write docstrings for all functions, methods, and classes
- Add appropriate error handling
- Keep functions and methods small and focused

## Testing

- Add tests for new features
- Ensure all tests pass before submitting a pull request
- Run tests with:
  ```
  python -m unittest discover tests
  ```

## Documentation

- Update the README.md file with any new features or changes
- Add docstrings to all new functions, methods, and classes
- Update the CHANGELOG.md file with your changes

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Update the CHANGELOG.md with details of changes
3. The version number will be updated by the maintainer
4. Your pull request will be merged once it has been reviewed and approved

## Feature Requests and Bug Reports

Please use the GitHub issue tracker to submit feature requests and bug reports.

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.
