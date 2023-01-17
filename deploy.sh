# Collect static
python manage.py collectstatic

# Apply DB Migrations
python manage.py migrate 

# Create Superuser if doesn't exist
python manage.py ensure_adminuser --username=admin \
    --email=admin@example.com \
    --password=$DJANGO_SUPERUSER_PASSWORD

# gunicorn quizapp.asgi:application -k uvicorn.workers.UvicornWorker \
#     -w 1 --bind 0.0.0.0:80 \
#     --bind 0.0.0.0:443

uvicorn quizapp.asgi:application --host 0.0.0.0 --port 10000