#!/bin/bash
set -e


python manage.py migrate
python manage.py loaddata persons_fixture.json
python manage.py collectstatic --noinput

gunicorn config.wsgi -b :8000
      
exec "$@"
