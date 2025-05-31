#!/bin/bash
echo "Testing CTchargen installation..."
source ./venv/bin/activate
python scripts/test_installation.py
read -p "Press Enter to continue..."
