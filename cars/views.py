from django.shortcuts import render
from utils.helpers import requete
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.http import HttpResponse
from . import forms
def CarHomePage(request):
    cars= requete("SELECT * FROM vehicule;").fetchall()
    return render(request, 'cars/index.html',{'cars':cars,'title': 'ACCUEIL VEHICULES'})

#Ouverture & Soumission du formulaire d'ajout de véhicule
def NewCarSubmit(request):
    print(request.POST)
    if request.POST:
        # Traitez les données soumises par le formulaire
        marque = request.POST['marque']
        modele = request.POST['modele']
        prix_par_jour = request.POST['prix_par_jour']
        #L'identifiant de l'administrateur connecté
        id_admin = 1
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
    cars= requete("SELECT * FROM vehicule;").fetchall()
    for car in cars:
        if car[0] == id:
            return render(request, 'cars/car.html', {'car':car,'title': car[1]+" "+car[2]})
    return render(request, 'error.html',{'error':'Véhicule non trouvable','title':'404!!! Page non trouvé'})

def DeleteCar(request,id,*args,**kwargs):
    
    requete("""
            DELETE
            FROM vehicule
            WHERE id_vehicule = {}
            """.format(id)
            )
    cars= requete("SELECT * FROM vehicule;").fetchall()
    return render(request, 'cars/index.html',{'cars':cars})
