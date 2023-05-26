from django.core.management.base import BaseCommand
from reservations.views import CREATE_volTable
from reservations.views import CREATE_carTable

class Command(BaseCommand):
    help = 'Create the Vol table in the database.'

    def handle(self, *args, **options):
        CREATE_volTable()
        CREATE_carTable()
        