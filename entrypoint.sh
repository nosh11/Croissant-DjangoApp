#!/bin/sh

set -e  # エラーが発生した場合にスクリプトを終了

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py shell < /app/create_superuser.py

gunicorn --workers 2 --threads 4 --timeout 60 --access-logfile \
    '-' --error-logfile '-' --bind=0.0.0.0:8000 croissant.wsgi