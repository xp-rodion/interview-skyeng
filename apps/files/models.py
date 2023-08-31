from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import User
from core.models import UUIDPrimaryModel


class File(UUIDPrimaryModel):

    CREATED = 1
    RECREATED = 2
    DELETED = 3

    STATUSES = (
        ('Создан', CREATED),
        ('Перезаписан', RECREATED),
        ('Удален', DELETED),
    )

    user = models.ForeignKey('Пользователь', to=User, on_delete=models.CASCADE)
    py_file = models.FileField('Python файл', validators=[FileExtensionValidator(["py"])])
    status = models.SmallIntegerField('Статус', choices=STATUSES, default=CREATED)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"