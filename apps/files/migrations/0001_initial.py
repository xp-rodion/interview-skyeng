# Generated by Django 3.2 on 2023-09-04 12:57

import django.core.validators
from django.db import migrations, models
import files.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Когда создан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Когда изменён')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('py_file', models.FileField(blank=True, null=True, upload_to=files.models.get_upload_path, validators=[django.core.validators.FileExtensionValidator(['py'])], verbose_name='Python файл')),
                ('status', models.SmallIntegerField(choices=[(1, 'Создан'), (2, 'Перезаписан'), (3, 'Удален')], default=1, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
