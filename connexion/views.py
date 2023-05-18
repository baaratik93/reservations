from django.shortcuts import render,redirect
from django.http import HttpRequest
from . import forms
# Create your views here.
def LoginUser(request):
    return render(request, 'connexion/login.html', {'formulaire': forms.LoginForm(),'title': 'Connexion utilisateur'})

def SigninUser(request):
    return render(request, 'connexion/signin.html', {'formulaire': forms.SigninForm(),'title': 'Inscription utilisateur'})

def index(request):
    redirect()
    return render(request,'connexion/login.html')