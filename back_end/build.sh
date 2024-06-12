#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requierements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
pytohn manage.py makemigrations user
pytohn manage.py makemigrations contact_book
pytohn manage.py makemigrations vehicles
python manage.py migrate
