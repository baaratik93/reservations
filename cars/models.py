from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    mot_de_passe = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

class Administrateur(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Client(models.Model):
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Vehicule(models.Model):
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    prix_par_jour = models.DecimalField(max_digits=10, decimal_places=2)
    id_admin = models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    photo = models.BinaryField()

class Reservation(models.Model):
    date_reservation = models.DateField()
    id_admin = models.ForeignKey(Administrateur, null=True, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)

class DetailsReservation(models.Model):
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    date_recuperation = models.DateField()
    date_retour = models.DateField()
    
    
class Car(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    mileage = models.IntegerField()
    price = models.IntegerField()
