# from django.core.management.base import BaseCommand
# import json
# from amadeus import Client, ResponseError
# from decimal import Decimal

# class Command(BaseCommand):
    # help = 'Insert data from a JSON file into the database using Django SQL'

    # def handle(self, *args, **options):
        
        

    #     amadeus = Client(
    #         client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
    #         client_secret='i7Npu291wpGAexgu'
    #     )

    #     try:
    #         '''
    #         Find the cheapest flights from SYD to BKK
    #         '''
    #         response = amadeus.shopping.flight_offers_search.get(
    #             originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2023-06-01', adults=1)
    #         print(response.data)
    #         for item in response.data:
    #             prix_value = Decimal(item['price']['total'])

    #             my_model = Vol(
    #                 type=item['type'],
    #                 source=item['source'],
    #                 heure_depart=item['itineraries'][0]['segments'][0]['departure']['at'],
    #                 heure_arrivee=item['itineraries'][0]['segments'][0]['arrival']['at'],
    #                 prix=prix_value
    #                 )
    #             my_model.save()
    #             print(my_model)
    #     except ResponseError as error:
    #         raise error
        
            
        
