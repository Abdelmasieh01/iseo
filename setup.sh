#!/bin/bash
# ISEO Website — Quick Setup Script
# Run this once to set up the project

echo "=== ISEO Website Setup ==="

# 1. Install Django
pip install django

# 2. Run migrations (creates the database)
python manage.py makemigrations
python manage.py migrate

# 3. Load partner university data
python manage.py loaddata iseo/fixtures/universities.json

# 4. Create a superuser for the admin panel
echo ""
echo "Creating admin user (for /admin panel)..."
python manage.py createsuperuser

echo ""
echo "=== Setup Complete ==="
echo "Run the server with: python manage.py runserver"
echo "Then open: http://127.0.0.1:8000"
echo "Admin panel: http://127.0.0.1:8000/admin"
