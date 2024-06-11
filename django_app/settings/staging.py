# pylint: disable=missing-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import
from django_app.settings.prod import *

INSTALLED_APPS += ["django_s3_sqlite"]

DATABASES = {
    "default": {
        "ENGINE": "django_s3_sqlite",
        "NAME": "django-app-staging.db",
        "BUCKET": AWS_STORAGE_BUCKET_NAME,
        "AWS_S3_ACCESS_KEY": AWS_ACCESS_KEY_ID,  # optional, to lock down your S3 bucket to an IAM user
        "AWS_S3_ACCESS_SECRET": AWS_SECRET_ACCESS_KEY,  # optional, to lock down your S3 bucket to an IAM user
    }
}
