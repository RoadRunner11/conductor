from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Bootstrap a VM with some starting data'

    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.create_superuser('matt', 'noreply@nowhere.com', 'secret')
