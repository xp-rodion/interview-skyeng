import os

from celery import Celery, schedules
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'create_report': {
        'task': 'files.tasks.create_report',
        'schedule': timedelta(seconds=5),
    },
    'send_report': {
        'task': 'reports.tasks.send_report',
        'schedule': timedelta(seconds=5),
    },
}