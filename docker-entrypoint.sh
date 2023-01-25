#!/bin/bash
set -e

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec uwsgi --ini ./uwsgi.ini
