from django.db import models
from apps.planet.models import Planet

# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Producer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    release_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    producers = models.ManyToManyField(Producer)
    planets = models.ManyToManyField(Planet)
