from django.db import models

from files.models import File
from core.models import UUIDPrimaryModel, TimeStampedModel


class Report(UUIDPrimaryModel, TimeStampedModel):
    """
    Модель, отвечающая за оповещение и логирование файла пользователя
    """

    CREATED = 1
    POSTED = 2
    ERROR = 3

    STATUSES = (
        (CREATED, 'Создан'),
        (POSTED, 'Отправлен'),
        (ERROR, 'Ошибка'),
    )

    title = models.CharField('Название отчета', max_length=128, blank=True, null=True)
    description = models.TextField('Описание отчета на почту', max_length=512, blank=True, null=True)
    file = models.ForeignKey(File, verbose_name='Файл', on_delete=models.CASCADE)
    status = models.SmallIntegerField('Статус', choices=STATUSES, default=CREATED)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.title = f'Отчет по {self.file.title} - py-file: {self.file.py_file.name.split("/")[-1]}'
        return super().save()

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'