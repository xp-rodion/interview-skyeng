from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from core.models import UUIDPrimaryModel
from core.mixins import PermissionsMixin
from core.managers import UserManager


class User(UUIDPrimaryModel, AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя
    """
    email = models.EmailField('Email', unique=True)
    last_login = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'