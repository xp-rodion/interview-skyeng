from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import User
from core.models import UUIDPrimaryModel, TimeStampedModel

def get_upload_path(instance, filename) -> str:
    """Функция, которая формирует путь до сохранения файла, папка для каждого объекта несет uid объекта"""
    return f"{instance.pk}/{filename}"


class File(UUIDPrimaryModel, TimeStampedModel):

    """
    Модель, отвечающее за загрузку файла, сам файл внутри может быть изменяться (засчет чего меняется статус модели)
    """

    CREATED = 1
    RECREATED = 2
    DELETED = 3

    STATUSES = (
        (CREATED, 'Создан'),
        (RECREATED, 'Перезаписан'),
        (DELETED, 'Удален'),
    )

    title = models.CharField('Название', max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    py_file = models.FileField('Python файл', upload_to=get_upload_path, validators=[FileExtensionValidator(['py'])], blank=True, null=True)
    status = models.SmallIntegerField('Статус', choices=STATUSES, default=CREATED)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.py_file:
            self.status = self.DELETED

        if None in (self.created_at, self.modified_at):
            return super().save()

        if self.modified_at > self.created_at:
            self.status = self.RECREATED

        return super().save()