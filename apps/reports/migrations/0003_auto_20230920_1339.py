# Generated by Django 3.2 on 2023-09-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20230904_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание отчета на почту'),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Название отчета'),
        ),
    ]
