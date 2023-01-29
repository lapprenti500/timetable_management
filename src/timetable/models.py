from django.db import models


# Create your models here.
class Dept(models.Model):
    nom_dpt = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Département"
    def __str__(self):
        return self.nom_dpt



class Filiere(models.Model):
    nom_filiere = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Filière"
    def __str__(self):
        return self.nom_filiere


class Promo(models.Model):
    nom_promo = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Promotion"
    def __str__(self):
        return self.nom_promo


class Cours(models.Model):
    identifiant = models.CharField(max_length=50)
    libelle = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Cour"
    def __str__(self):
        return self.libelle


class Salle(models.Model):
    nom = models.CharField(max_length=20)
    description = models.CharField(max_length=20)


    class Meta:
        verbose_name = "Salle"
    def __str__(self):
        return f"{self.nom} {self.description}"


class Prof(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)


    class Meta:
        verbose_name = "Professeur"
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Creneau(models.Model):
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, default=None)
    cours = models.ForeignKey(Cours, on_delete=models.SET_NULL, null=True)
    prof = models.ForeignKey(Prof, on_delete=models.SET_NULL, null=True)
    salle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()







