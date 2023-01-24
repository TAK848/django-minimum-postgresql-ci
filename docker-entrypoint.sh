#!/bin/bash
set -e

if [ -n "$1" ]; then
    exec "$@"
fi

python manage.py makemigrations
python manage.py migrate

exec uwsgi --ini ./uwsgi.ini
