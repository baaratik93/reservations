from django.shortcuts import render,redirect
from utils.helpers import requete
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.http import HttpResponse
from . import forms
from django.db import connection
import requests
import json
import random
from django.http import JsonResponse
from faker import Faker

def CarHomePage(request):
    with connection.cursor() as cursor:
        # Exécution de la requête SQL
        cursor.execute("SELECT * FROM vehicule;")
        # columns = [col[0] for col in cursor.description]
        # cars = [
        #     dict(zip(columns, row))
        #     for row in cursor.fetchall()
        # ]
        # return HttpResponse([cars])
        # # Récupération des résultats
        cars = cursor.fetchall()
        cars= requete("SELECT * FROM vehicule;").fetchall()
        # if request.session['user']:
        #     user = request.session['user']
        # else:
        #     user =''
        # print(request.session['user'])
    return render(request, 'cars/index.html',{'cars':cars,'title': 'ACCUEIL VEHICULES'})

#Ouverture & Soumission du formulaire d'ajout de véhicule
def NewCarSubmit(request):
    print(request.session['user'][7])
    if 'jwt' not in request.session:
        return redirect('/connexion/login')
    if request.session['user'][7] != 'admin':
        return redirect('/cars')
    print(request.POST)
    if request.POST:
        # Traitez les données soumises par le formulaire
        marque = request.POST['marque']
        modele = request.POST['modele']
        prix_par_jour = request.POST['prix_par_jour']
        #L'identifiant de l'administrateur connecté
        id_admin = 2
        photo = request.FILES['photo']
        path = default_storage.save(photo, ContentFile(photo.read()))
        vehicule = (marque,modele,prix_par_jour,id_admin,path)
        requete("""
                INSERT 
                INTO vehicule(marque,modele,prix_par_jour,id_admin,photo)
                VALUES {}
                """.format(vehicule))
        cars= requete("SELECT * FROM vehicule;").fetchall()
        return render(request, 'cars/index.html',{'cars':cars})
    else:
        return render(request, 'cars/new.html', {'formulaire': forms.NewCarForm()})



def SingleCar(request,id,*args,**kwargs):
    if 'jwt' not in request.session:
        return redirect('/connexion/login')
    cars= requete("SELECT * FROM vehicule;").fetchall()
    for car in cars:
        if car[0] == id:
            return render(request, 'cars/car.html', {'car':car,'title': car[1]+" "+car[2]})
    return render(request, 'error.html',{'error':'Véhicule non trouvable','title':'404!!! Page non trouvé'})

def DeleteCar(request,id,*args,**kwargs):
    if 'jwt' not in request.session:
        return redirect('/connexion/login')
    if request.session['user'][7] != 'admin':
        return redirect('/cars')
    requete("""
            DELETE
            FROM vehicule
            WHERE id_vehicule = {}
            """.format(id)
            )
    cars= requete("SELECT * FROM vehicule;").fetchall()
    return render(request, 'cars/index.html',{'cars':cars})


def ReserverCar(request,id,*args,**kwargs):
    if 'jwt' not in request.session:
        return redirect('/connexion/login')
    cars= requete("SELECT * FROM vehicule;").fetchall()
    for car in cars:
        if car[0] == id:
            dictCar = {'marque': car[1], 'modele':car[2], 'prix':car[3],'image': car[5]}
            if 'reserved' in request.session:
                request.session['reserved'].append(dictCar)
            else:
                request.session['reserved'] = []
                request.session['reserved'].append(dictCar)
            request.session.save()
            # del request.session['reserved']

            return render(request, 'cars/index.html',{'cars':cars})
    

fake = Faker()

CAR_BRANDS = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes-Benz', 'Audi', 'Nissan', 'Lamborghini']

image_corres = [
    {'name': 'Audi', 'url': 'https://images.unsplash.com/photo-1616422285623-13ff0162193c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=731&q=80'},
    {'name': 'BMW', 'url': 'https://unsplash.com/fr/photos/Y8-H19uSx-Y'},
    {'name': 'Honda', 'url': 'https://unsplash.com/fr/photos/O7WzqmeYoqc'},
    {'name': 'Toyota', 'url': 'https://unsplash.com/fr/photos/AICttBivH5w'},
    {'name': 'Ford', 'url': 'https://unsplash.com/fr/photos/a4S6KUuLeoM'},
    {'name': 'Chevrolet', 'url': 'https://images.unsplash.com/photo-1590510655579-26ceebea7986?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=747&q=80'},
    {'name': 'Mercedes-Benz', 'url': 'https://images.unsplash.com/photo-1622551997608-400d763b0f64?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=735&q=80'},
    {'name': 'Nissan', 'url': 'https://images.unsplash.com/photo-1581540222194-0def2dda95b8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'},
    {'name': 'Lamborghini', 'url': 'https://unsplash.com/fr/photos/pRlbr85Jvqw'}
]


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
cars = json.loads(content)

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
      for car in cars:
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
