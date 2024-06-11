#!/bin/sh
set -e
coverage run --source 'django_app/' manage.py test "$@"
coverage report