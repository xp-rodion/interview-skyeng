from users.models import User

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        print('Пользователи удалены!')