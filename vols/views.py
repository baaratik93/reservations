from django.shortcuts import render
from django.db import connection
from amadeus import Client, ResponseError

# Create your views here.

def CREATE_volTable():
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE reservations_Vol (
                id INT auto_increment NOT NULL,
                type VARCHAR(255) NOT NULL,
                source VARCHAR(100) NOT NULL,
                heure_depart DATETIME NOT NULL,
                heure_arrivee DATETIME NOT NULL,
                prix DECIMAL(10, 4) NOT NULL,
                aeroport_depart VARCHAR(10) NOT NULL,
                aeroport_arrivee VARCHAR(10) NOT NULL,
                CONSTRAINT pk_vol PRIMARY KEY (id)
            );
        """)
        amadeus = Client(
            client_id='m6DhvrLb1NAoGygATfeD8lEpMKlQxva8',
            client_secret='i7Npu291wpGAexgu'
        )

        try:
            '''
            Find the cheapest flights from SYD to BKK
            '''
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode='SYD', destinationLocationCode='BKK', departureDate='2023-06-01', adults=1)
            # print(response.data)
            for item in response.data:
              values=(item['type'], item['source'],item['itineraries'][0]['segments'][0]['departure']['at'],item['itineraries'][0]['segments'][0]['arrival']['at'], item['price']['total'], item['itineraries'][0]['segments'][0]['departure']['iataCode'],item['itineraries'][0]['segments'][0]['arrival']['iataCode'])
              cursor.execute(
                '''
                INSERT INTO reservations_Vol(type, source, heure_depart, heure_arrivee, prix, aeroport_depart, aeroport_arrivee)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', values
              )
        except ResponseError as error:
            raise error
    
    
