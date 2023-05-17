from django.shortcuts import render
from utils.helpers import requete
from . import forms
from .models import Image
def CarHomePage(request):
    cars= requete("SELECT * FROM vehicule;").fetchall()
    return render(request, 'cars/index.html',{'cars':cars})

#Ouverture & Soumission du formulaire d'ajout de véhicule
def NewCarSubmit(request):
    print(request.POST)
    if request.POST:
        marque = request.POST['marque']
        modele = request.POST['modele']
        prix_par_jour = request.POST['prix_par_jour']
        #L'identifiant de l'administrateur connecté
        id_admin = 1
        form = forms.NewCarForm(request.POST, request.FILES)
        photo = form
        
        print("Here",photo)
        # Traitez les données soumises par le formulaire
        # vehicule = (marque,modele,prix_par_jour,id_admin)
        with open(request.FILES['photo'], "r") as image_file:
            image_data = image_file.read()
            print("Heres",image_data)
        # sql = "INSERT INTO vehicule(marque,modele,prix_par_jour,id_admin) VALUES {}".format(vehicule)
        # requete(sql)
        cars= requete("SELECT * FROM vehicule;").fetchall()
        return render(request, 'cars/index.html',{'cars':cars})
    else:
        return render(request, 'cars/new.html', {'formulaire': forms.NewCarForm()})



    
