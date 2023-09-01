from django.db import models

from files.models import File
from core.models import UUIDPrimaryModel, TimeStampedModel


class Report(UUIDPrimaryModel, TimeStampedModel):
    """
    Модель, отвечающая за оповещение и логирование файла пользователя
    """

    CREATED = 1
    POSTED = 2

    STATUSES = (
        ('Создан', CREATED),
        ('Отправлен', POSTED),
    )

    title = models.CharField('Название отчета', max_length=128, blank=True)
    description = models.TextField('Описание отчета на почту', max_length=512)
    file = models.ForeignKey(File, verbose_name='Файл', on_delete=models.CASCADE)
    status = models.SmallIntegerField('Статус', choices=STATUSES, default=CREATED)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.title:
            self.title = f'Отчет по {self.file.title} - py-file: {self.file.py_file.name}'

        return super().save()

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'