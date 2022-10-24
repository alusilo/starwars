from django.db import models
from apps.planet.models import Planet

# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.TextField()


class ProductionCompany(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Film(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    opening_text = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    production_companies = models.ManyToManyField(ProductionCompany)
    planets = models.ManyToManyField(Planet)
