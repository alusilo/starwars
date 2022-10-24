from django.db import models
from apps.film.models import Film

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200, unique=True)
    gender = models.CharField(max_length=30)
    specie = models.CharField(max_length=30)
    height = models.FloatField()
    description = models.TextField()
    films = models.ManyToManyField(Film)
