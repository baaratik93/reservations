from django.shortcuts import render,redirect
from utils.helpers import requete
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.http import HttpResponse
from . import forms
from django.db import connection

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
            dictCar = {'id': car[0],'marque': car[1], 'modele':car[2], 'prix':car[3],'image': car[5]}
            if 'reserved' in request.session:
                request.session['reserved'].append(dictCar)
            else:
                request.session['reserved'] = []
                request.session['reserved'].append(dictCar)
            request.session.save()
            # del request.session['reserved']

            return render(request, 'cars/index.html',{'cars':cars})
    
