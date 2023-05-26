from django.shortcuts import render
from . import forms
import json
import requests

def HomePage(request):
    return render(request, 'index.html',{'title': "PAGE D'ACCUEIL"})

def AddReservation(request):
    total_prix = sum([r['prix'] for r in request.session['reserved']])
    return render(request, 'reservation.html',{'title': "RESERVATION",'total_prix':total_prix,'forms':forms.ReservationForm})
# BEGIN TRANSACTION;

# WITH reser AS (
#     INSERT INTO reservation (date_reservation, id_client)
#     VALUES ('2023-05-21', 8)
#     RETURNING id_reservation
# )
# INSERT INTO details_reservation (id_vehicule, id_reservation, date_recuperation, date_retour)
# SELECT 30, id_reservation, '2023-06-25', '2023-06-30'
# FROM reser;

# COMMIT;




from amadeus import Client, ResponseError

from django.db import connection

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
    



def random_car(request):
    data = []
    image_url = ""
    for _ in range(1000):
        marque = random.choice(CAR_BRANDS)
        modele = fake.word()
        for image in image_corres:
            if marque == image['name']:
                image_url = image['url']

        voiture = {
            'marque': marque,
            'modele': modele,
            'annee': random.randint(2000, 2023),
            'prix_journee': random.uniform(50, 300),
            'image_url': image_url
        }
        data.append(voiture)
    response = JsonResponse(data, safe=False)

    return response

response = random_car(requests)
content = response.content.decode('utf-8')
print(len(content))
data = json.loads(content)
print(len(data))
def CREATE_carTable():
  with connection.cursor() as cursor:
    try:
      cursor.execute('''
          CREATE TABLE reservations_Car(
            id INT auto_increment NOT NULL,
            marque VARCHAR(50) NOT NULL,
            modele VARCHAR(25) NOT NULL,
            annee INT(4) NOT NULL,
            prix_journee DECIMAL(10, 4) NOT NULL,
            image_url VARCHAR(255) NOT NULL,
            CONSTRAINT pk_car PRIMARY KEY (id)
            );
            ''')
      for car in data:
          marque = car['marque']
          modele = car['modele']
          annee = car['annee']
          prix_journee = car['prix_journee']
          image_url = car['image_url']
          values=(marque, modele, annee, prix_journee, image_url)
          
          cursor.execute('''
            INSERT INTO reservations_Car(marque, modele, annee, prix_journee, image_url)
            VALUES(%s, %s, %s, %s, %s)
            
                        ''',values)
    except ResponseError as error:
      raise error
        
