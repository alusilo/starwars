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
    
    
class FilmDirector(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class FilmProducer(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)


class FilmPlanet(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
