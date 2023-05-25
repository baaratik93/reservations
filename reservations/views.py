from django.shortcuts import render
from . import forms

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