# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
import json
import os

import dj_database_url as dj_url

from django_app.settings.base import *

DEBUG = json.loads(os.environ.get("DEBUG", "false"))
ALLOWED_HOSTS = json.loads(os.environ.get("ALLOWED_HOSTS", "[]"))

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Database connection over DJANGO_APP_DB_URI
DJANGO_APP_DB_URI = os.getenv("DJANGO_APP_DB_URI")
DATABASES = {"default": dj_url.config(default=DJANGO_APP_DB_URI)}


# Django Storages AWS config
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

# S3 static settings
AWS_LOCATION = "static"

if not DEBUG:
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
    INSTALLED_APPS += ["health_check.contrib.s3boto3_storage"]
