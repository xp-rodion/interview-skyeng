# Generated by Django 3.2 on 2023-09-04 12:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Когда создан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Когда изменён')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='Название отчета')),
                ('description', models.TextField(max_length=512, verbose_name='Описание отчета на почту')),
                ('status', models.SmallIntegerField(choices=[('Создан', 1), ('Отправлен', 2)], default=1, verbose_name='Статус')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.file', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
