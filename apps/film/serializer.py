from rest_framework import serializers
from apps.film.models import Film, Director, ProductionCompany
from apps.planet.serializer import PlanetSerializer


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ProductionCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionCompany
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    production_companies = ProductionCompanySerializer(many=True)
    planets = PlanetSerializer(many=True)
    class Meta:
        model = Film
        fields = '__all__'