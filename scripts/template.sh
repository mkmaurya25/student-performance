#!/bin/bash

# Main project directory
mkdir student-performance
cd student-performance

# Data folders
mkdir -p data/raw data/processed

# Source code folders
mkdir -p src/data src/models src/utils

# Notebooks, tests, models, config, and scripts
mkdir notebooks tests models config scripts

# GitHub Actions workflows
mkdir -p .github/workflows

# Placeholder files
touch README.md requirements.txt Dockerfile setup.py

echo "Project structure created successfully!"
