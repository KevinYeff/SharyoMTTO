#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requierements.txt

# Clean up old migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Drop and recreate the database (specific to PostgreSQL)
psql -c "DROP DATABASE IF EXISTS sharyomtto_pg;" -U $DATABASE_USER
psql -c "CREATE DATABASE sharyomtto_pg;" -U $DATABASE_USER

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations user contact_book vehicles
python manage.py migrate


# Create a superuser if none exists
if [ -z "$(python manage.py shell -c 'from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).count())')" ]; then
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
fi
