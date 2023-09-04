import uuid

from django.db import models


class UUIDPrimaryModel(models.Model):
    """
    Модель для представления UUID
    """
    uid = models.UUIDField('UUID', default=uuid.uuid4, primary_key=True)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Модель с датой и временем создания и изменения
    """
    created_at = models.DateTimeField('Когда создан', auto_now_add=True)
    modified_at = models.DateTimeField('Когда изменён', auto_now=True)

    class Meta:
        abstract = True

