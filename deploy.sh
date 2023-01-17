# Collect static
python manage.py collectstatic

# Apply DB Migrations
python manage.py migrate 

# Create Superuser if doesn't exist
python manage.py ensure_adminuser --username=admin \
    --email=admin@example.com \
    --password=$DJANGO_SUPERUSER_PASSWORD

uvicorn quizapp.asgi:application --host 0.0.0.0