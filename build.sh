#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r back_end/requierements.txt

# Convert static asset files
python back_end/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python back_end/manage.py migrate
