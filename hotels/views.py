from django.shortcuts import render
from django.http import JsonResponse
from faker import Faker
import json
import random
from django.db import connection
import requests

# Create your views here.


image_available = [
    {"name":"chambre_simple", "url": "https://images.unsplash.com/flagged/photo-1556438758-8d49568ce18e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1174&q=80"},
    {"name": "chambre_double", "url": "https://unsplash.com/fr/photos/_Sr6plc5dpQ"},
    {"name": "chambre_de_luxe", "url":"https://images.unsplash.com/photo-1519710889408-a67e1c7e0452?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80"},
    {"name":"suite", "url":"https://unsplash.com/fr/photos/AOBEP4Qq00s"}
]

def random_hotel(request):
    fake = Faker()
    hotels = []
    for _ in range(100):
        room=random.choice(["chambre_simple", "chambre_double", "chambre_de_luxe", "suite"])
        for img_url in image_available:
            if room == img_url['name']:
                image_url = img_url['url']
            
                hotel = {
                    "name": fake.company(),
                    "room": room,
                    "description": fake.text(),
                    "capacity": fake.random_int(min=1, max=6),
                    "address": fake.address(),
                    "city": fake.city(),
                    "country": fake.country(),
                    "image_url" : image_url
                }
                hotels.append(hotel)
            
                datas = JsonResponse(hotels, safe=False)
        
    return datas
      



response = random_hotel(requests)
content = response.content.decode('utf-8')
hotels = json.loads(content)

def CREATE_hotelTable():
  with connection.cursor() as cursor:
      cursor.execute('''
          CREATE TABLE reservations_Hotel(
            id INT auto_increment NOT NULL,
            nom VARCHAR(50) NOT NULL, 
            chambre VARCHAR(50) NOT NULL,
            description VARCHAR(255) NOT NULL,
            capacite INT NOT NULL,
            adresse VARCHAR(100) NOT NULL,
            ville VARCHAR(50) NOT NULL,
            pays VARCHAR(100) NOT NULL,
            image_url VARCHAR(255) NOT NULL,
            CONSTRAINT pk_hotel PRIMARY KEY (id)
          );
          ''')
      for hotel in hotels:   
        nom = hotel["name"]
        # print(nom)
        chambre = hotel['room']
        description = hotel['description']
        capacite = hotel['capacity']
        adresse = hotel['address']
        ville = hotel['city']
        pays = hotel['country']
        image_url = hotel['image_url']
        values = (nom, chambre, description, capacite, adresse, ville, pays, image_url)
        cursor.execute('''
        INSERT INTO reservations_Hotel(nom, chambre, description, capacite, adresse, ville, pays, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ''', values)
