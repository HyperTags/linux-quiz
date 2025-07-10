#!/bin/bash
# This script will make the quiz executable during setup

echo "Setting executable permissions..."
chmod +x linux.py

# Also make this setup script executable (for future runs)
chmod +x setup.sh

echo -e "\nNow you can run either:"
echo -e "  ./linux.py"
echo -e "  python3 linux.py\n"