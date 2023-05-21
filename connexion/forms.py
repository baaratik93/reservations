from django import forms
class LoginForm(forms.Form):
    login = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput())
    
    
class SigninForm(forms.Form):
    nom = forms.CharField(label="Nom")
    prenom = forms.CharField(label="Prénom")
    login = forms.CharField(label="Nom d'utilisateur")
    telephone = forms.CharField(label="Téléphone")
    # photo= forms.ImageField(label="Photo")
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput())
    cpassword = forms.CharField(label='Confirmer mot de passe',widget=forms.PasswordInput())
    