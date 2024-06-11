from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_app.apps.accounts.managers import UserManager


class User(AbstractUser):
    class ProfileChoices(models.IntegerChoices):
        COORDENADOR = (1, "Coordenador")
        DESENVOLVEDOR = (2, "Desenvolvedor")

    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
