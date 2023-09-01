from django.contrib import admin
from reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'file', 'status')
