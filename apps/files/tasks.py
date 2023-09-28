from django.db.models import Q

from config.celery import schedules, app

from files.models import File
from reports.models import Report
from core.utils import check_code


@app.task(queue="report")
def create_report():
    filtered_files = File.objects.filter(Q(status__in=(File.CREATED, File.RECREATED)) & Q(verified=False))
    for file in filtered_files:
        desc = check_code(file.py_file)
        Report.objects.get_or_create(
            description=desc,
            file=file,
        )
        print("Создаю репорты!")
        file.verified = True
        file.save()
