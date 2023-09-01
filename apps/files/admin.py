from django.contrib import admin
from files.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'py_file', 'status')
