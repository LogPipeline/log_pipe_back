#!/bin/sh

set -e 

echo "${0}: running migrations. :"

python manage.py makemigrations authentication
python manage.py makemigrations dashboard
python manage.py migrate --noinput

echo "${0} : collect staticfile "
python3 manage.py collectstatic --noinput

gunicorn config.wsgi --bind 0.0.0.0:8000
