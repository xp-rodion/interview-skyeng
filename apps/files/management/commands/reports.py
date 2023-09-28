from django.core.management.base import BaseCommand
from django.conf import settings

from files.models import File
from reports.models import Report


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Использование команды, для создания нового потока приложения,
        который отвечает за создание Report'ов и отложенных задач
        """

        files = File.objects.filter(status__in=(File.CREATED, File.RECREATED))
        for file in files:

            with open(f"{settings.MEDIA_ROOT}/{file.py_file.name}", "r") as py_file:
                py_code = "\n".join(py_file.readlines())
                py_list = py_file.readlines()
                # print(py_file.readlines())
            #result = eval(py_code)
            # report = Report.objects.get_or_create(
            #     description='',
            #     file=file,
            # )
            #print(result.__dict__)
            print(py_list)