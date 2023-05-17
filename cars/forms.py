from django import forms
class NewCarForm(forms.Form):
    marque = forms.CharField(label='Marque')
    modele = forms.CharField(label='Modèle')
    prix_par_jour = forms.CharField(label='Prix/Jour')
    photo = forms.ImageField(label='Image')