from enum import unique
from statistics import mode
from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
