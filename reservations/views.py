from django.shortcuts import render
from . import forms
import json
import requests
# import JsonResponse
from django.db import connection
import random

import random
from django.http import JsonResponse
from faker import Faker


def HomePage(request):
    return render(request, 'index.html',{'title': "PAGE D'ACCUEIL"})

def AddReservation(request):
    total_prix = sum([r['prix'] for r in request.session['reserved']])
    return render(request, 'reservation.html',{'title': "RESERVATION",'total_prix':total_prix,'forms':forms.ReservationForm})

def CREATE_OthersTables():
    with connection.cursor() as cursor:
        # cursor.execute('''
        #     CREATE TABLE reservations_Utilisateur(
        #         id INT auto_increment NOT NULL,
        #         nom VARCHAR(30) NOT NULL,
        #         prenom VARCHAR(50) NOT NULL,
        #         telephone VARCHAR(10) NOT NULL,
        #         login VARCHAR(15) NOT NULL,
        #         password VARCHAR(15) NOT NULL,
        #         role VARCHAR(20) NOT NULL,
        #         id_reservation INT,
        #         CONSTRAINT fk_reservationUser FOREIGN KEY(id_reservation) references reservations_Reservation(id),
        #         CONSTRAINT pk_user PRIMARY KEY (id)
        #     );
        #              ''')
        # cursor.execute('''
        #     CREATE TABLE reservations_Reservation(
        #         id INT auto_increment NOT NULL,
        #         date DATE NOT NULL,
        #         id_user INT NOT NULL,
        #         type_reservation VARCHAR(30) NOT NULL,
        #         etat_reservation ENUM('en attente','validé','annulé') NOT NULL,
        #         CONSTRAINT pk_reservation PRIMARY KEY (id)
        #     );
        #                ''')
        
        # cursor.execute('''
        #     CREATE TABLE reservations_Billet(
        #         id INT auto_increment NOT NULL,
        #         id_vol INT NOT NULL,
        #         id_reservation INT NOT NULL,
        #         CONSTRAINT fk_vol FOREIGN KEY (id_vol) references reservations_Vol(id),
        #         CONSTRAINT fk_reservation FOREIGN KEY (id_reservation) references reservations_Reservation(id),
        #         CONSTRAINT pk_billet PRIMARY KEY (id)
        #     );
        #                ''')
        
        # cursor.execute('''
        #     CREATE TABLE reservations_Details(
        #         id INT auto_increment NOT NULL,
        #         date_recup DATE NOT NULL,
        #         date_retour DATE NOT NULL,
        #         id_car INT NOT NULL,
        #         id_reservation INT NOT NULL,
        #         CONSTRAINT fk_car FOREIGN KEY (id_car) references reservations_Car (id),
        #         CONSTRAINT fk_reservation2 FOREIGN KEY (id_reservation) references reservations_Reservation(id),
        #         CONSTRAINT pk_details PRIMARY KEY(id)
        #     );
        #                ''')
        
        # cursor.execute('''
        #     CREATE TABLE reservations_Paiement(
        #         id INT auto_increment NOT NULL,
        #         montant INT NOT NULL,
        #         nom_agence VARCHAR(30) NOT NULL,
        #         CONSTRAINT pk_payement PRIMARY KEY(id)
        #     ); 
        #                ''')
        
        # cursor.execute('''
        #     CREATE TABLE reservations_detailsPaiement(
        #         id INT auto_increment NOT NULL,
        #         id_paiement INT NOT NULL,
        #         id_reservation INT NOT NULL,
        #         CONSTRAINT fk_paiement FOREIGN KEY (id_paiement) references reservations_Paiement(id),
        #         CONSTRAINT fk_reservation1 FOREIGN KEY (id_reservation) references reservations_Reservation(id),
        #         CONSTRAINT pk_detailsPaiement PRIMARY KEY(id)
        #     );
        #         ''')
        
        # cursor.execute('''
        #     ALTER TABLE reservations_Hotel
        #     ADD COLUMN id_reservation INT,
        #     ADD CONSTRAINT fk_reservationRoom FOREIGN KEY (id_reservation) references reservations_Reservation(id)
        #                ''')
        pass






