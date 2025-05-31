#!/bin/bash
echo "Fixing frontend build issues..."
source ./venv/bin/activate
python scripts/fix_frontend_build.py
read -p "Press Enter to continue..."
