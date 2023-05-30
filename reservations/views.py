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









