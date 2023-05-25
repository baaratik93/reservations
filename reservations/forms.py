from django import forms
class ReservationForm(forms.Form):
    date_de_recuperation = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Date de récupération")
    date_de_retour = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),label="Date de retour")
    
    
    