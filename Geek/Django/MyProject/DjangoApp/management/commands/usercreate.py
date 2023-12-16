from django.core.management.base import BaseCommand
from DjangoApp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        user = User(name='XYI7I', email='xyi7i@example.com', password='secret', age=33, phone_number='123456789', address='123 Main St')
        user.save()
        self.stdout.write(f'{user}')
