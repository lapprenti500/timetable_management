from django.db import models


# Create your models here.
class Dept(models.Model):
    nom_dpt = models.CharField(max_length=100)


class Filiere(models.Model):
    nom_filiere = models.CharField(max_length=100)


class Promo(models.Model):
    nom_promo = models.CharField(max_length=20)


class Matiere(models.Model):
    id_matiere = models.CharField(max_length=50)
    libelle = models.CharField(max_length=100)


class Salle(models.Model):
    description = models.CharField(max_length=20)


class Prof(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)


class Creneau(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()






