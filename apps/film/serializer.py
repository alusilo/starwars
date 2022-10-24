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
<<<<<<< HEAD
=======
    director = DirectorSerializer()
    production_companies = ProductionCompanySerializer(many=True)
    planets = PlanetSerializer(many=True)
>>>>>>> 9f3652c4df2013d100cc7005c66322c2128950a6
    class Meta:
        model = Film
        fields = '__all__'