# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
import dj_database_url as dj_url

from django_app.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ["*"]
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DJANGO_APP_DB_URI = os.getenv("DJANGO_APP_DB_URI") or f"sqlite:///{BASE_DIR}/db.sqlite3"

DATABASES = {"default": dj_url.config(default=DJANGO_APP_DB_URI)}
