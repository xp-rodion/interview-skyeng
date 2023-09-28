from config.celery import schedules, app
from django.core.mail import send_mail
from django.conf import settings

from reports.models import Report


@app.task(queue="email")
def send_report():
    reports = Report.objects.filter(status=Report.CREATED)
    for report in reports:
        user_email = report.file.user.email
        subject = f'Отчет о проведенной проверке по "{report.file.title}"'
        message = report.description
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_email],
                fail_silently=False,
            )
            report.status = Report.POSTED
            print("Отправляю репорт")
        except OSError:
            report.status = Report.ERROR
            print("Ошибка отправки!")
        finally:
            report.save()