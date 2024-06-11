#!/bin/sh

python manage.py collectstatic --noinput -v3
python manage.py migrate --noinput
