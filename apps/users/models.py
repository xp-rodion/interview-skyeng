from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from core.models import UUIDPrimaryModel


class User(UUIDPrimaryModel, AbstractBaseUser):
    email = models.EmailField("Почта", unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"