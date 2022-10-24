from rest_framework import serializers
from apps.character.models import Character
from apps.film.serializer import FilmSerializer

class CharacterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True)
    class Meta:
        model = Character
        fields = '__all__'
