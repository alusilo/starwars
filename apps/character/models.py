from django.db import models
from apps.planet.models import Planet

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=200)
    height = models.FloatField()
    description = models.CharField(max_length=500)
    home_planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
