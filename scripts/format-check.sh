#!/bin/sh

black --check --diff django_app/
autopep8 --diff django_app/
isort --check --diff django_app/
