#!/bin/sh

APP_PORT=${APP_PORT:=8888}

./scripts/build.sh
python manage.py runserver 0.0.0.0:$APP_PORT
