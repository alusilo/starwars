from rest_framework import serializers
from apps.film.models import Film, FilmDirector, FilmProducer, FilmPlanet

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class FilmDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmDirector
        fields = '__all__'


class FilmProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmProducer
        fields = '__all__'


class FilmPlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPlanet
        fields = '__all__'
