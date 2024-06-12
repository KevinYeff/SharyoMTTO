#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requierements.txt

# Clean up old migrations
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Delete local SQLite database if it exists (adjust if needed for your setup)
if [ -f "db.sqlite3" ]; then
    rm db.sqlite3
fi

# Drop and recreate the database
python manage.py flush --no-input

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py makemigrations user contact_book vehicles
python manage.py migrate


# Create a superuser if none exists
if [ -z "$(python manage.py shell -c 'from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(is_superuser=True).count())')" ]; then
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
fi
