from django.core.management.base import BaseCommand
from hotels.views import CREATE_hotelTable
from cars.views import CREATE_carTable
from vols.views import CREATE_volTable
from reservations.views import CREATE_OthersTables



class Command(BaseCommand):
    help = 'Create the Vol table in the database.'

    def handle(self, *args, **options):
        # CREATE_volTable()
        # CREATE_carTable()
        # CREATE_hotelTable()
        CREATE_OthersTables()