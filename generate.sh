#!/bin/bash
# Character generation shell script for CTchargen
# This shell script provides a simple way to generate characters on Unix-like systems

echo "CTchargen - Classic Traveller Character Generator"
echo "================================================"

if [ $# -eq 0 ]; then
    echo "Generating 1 character with default settings..."
    python generate_characters.py
else
    python generate_characters.py "$@"
fi

echo ""
echo "Done!"
