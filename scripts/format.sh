#!/bin/sh

black django_app/
autopep8 --in-place django_app/
isort django_app/
