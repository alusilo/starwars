from rest_framework import serializers
from apps.film.models import Film, Director, Producer
from apps.planet.serializer import PlanetSerializer


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    producers = ProducerSerializer(many=True)
    planets = PlanetSerializer(many=True)
    class Meta:
        model = Film
        fields = '__all__'