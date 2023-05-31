from django.shortcuts import render
from django.http import HttpResponse

from . import forms

def HomePage(request):
    return render(request, 'index.html',{'title': "PAGE D'ACCUEIL"})

def AddReservation(request):
    total_prix = sum([r['prix'] for r in request.session['reserved']])
    return render(request, 'reservation.html',{'title': "RESERVATION",'total_prix':total_prix,'forms':forms.ReservationForm})

def Payement(request):
    if request.method == 'POST':
        # print(request.POST['date_de_retour'])
        return render(request, 'payement.html', {'debut': request.POST['date_de_recuperation'],'retour': request.POST['date_de_retour'],'prix_par_jour': request.POST['prix']})
    return render(request,'payement.html',{})
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