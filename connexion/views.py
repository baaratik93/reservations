from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import forms
from django.conf import settings
from utils.helpers import requete,crypter_mot_de_passe,coder_jwt,decoder_jwt,verifier_mot_de_passe

# Create your views here.
def LoginUser(request):
    if request.POST:
        users = requete("SELECT * FROM utilisateur")
        ExistLogin = False
        for user in users.fetchall():
            print(user)
            if user[5] == request.POST['login']:
                ExistLogin = True
                if verifier_mot_de_passe(request.POST['password'], user[6]):
                    jwt = coder_jwt({'id_utilisateur':user[0],'login':user[5],'role':user[7]})
                    print(jwt)
                    cars= requete("SELECT * FROM vehicule;").fetchall()
                    # return redirect('/cars/',{'cars':cars, 'jwt':jwt})
                    return render(request, 'cars/index.html',{'cars':cars,'title': 'ACCUEIL VEHICULES','jwt':jwt})
                else:
                    return render(request, 'connexion/login.html', {'formulaire': forms.LoginForm(),'title': 'Connexion utilisateur','error':'Mot de passe incorrect'})
        if not ExistLogin:
                   return render(request, 'connexion/login.html', {'formulaire': forms.LoginForm(),'title': 'Connexion utilisateur','error':"Ce login n'existe pas"})
    return render(request, 'connexion/login.html', {'formulaire': forms.LoginForm(),'title': 'Connexion utilisateur'})

def SigninUser(request):
    if request.POST:
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        login = request.POST['login']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if password == cpassword:
            # Hacher le mot de passe
            #Vérifier l'existant d'un même nom d'utilisateur
            users = requete("SELECT * FROM utilisateur").fetchall()
            test = False
            for user in users:
                if user[5] == login:
                    test = True
                    break
            if test:
                return render(request, 'connexion/signin.html', {'formulaire': forms.SigninForm(),'title': 'Inscription utilisateur','error':'Ce login existe déja'})
            else:
                # Enrégistrer l'utilisateur
                user = (nom,prenom,telephone,login,crypter_mot_de_passe(password),"client")
                sql = """
                
                BEGIN TRANSACTION;

                WITH nouvel_id AS(
                    INSERT INTO utilisateur(nom,prenom,telephone,login,mot_de_passe,role)
                    VALUES {}
                    RETURNING id_utilisateur
                )

                INSERT INTO client (id_utilisateur)
                SELECT id_utilisateur
                FROM nouvel_id;

                COMMIT;

                """.format(user)
                requete(sql)
        else:
            return render(request, 'connexion/signin.html', {'formulaire': forms.SigninForm(),'title': 'Inscription utilisateur','error':'Les mots de passent ne correspondent pas'})
        
    return render(request, 'connexion/signin.html', {'formulaire': forms.SigninForm(),'title': 'Inscription utilisateur'})

def index(request):
    redirect()
    return render(request,'connexion/login.html')