from rest_framework import serializers
from apps.character.models import Character
from apps.planet.serializer import PlanetSerializer

class CharacterSerializer(serializers.ModelSerializer):
    home_planet = PlanetSerializer()
    class Meta:
        model = Character
        fields = '__all__'
