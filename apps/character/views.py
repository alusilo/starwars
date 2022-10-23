from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.character.models import Character
from apps.character.serializer import CharacterSerializer

# Create your views here.
class CharacterListView(APIView):
    def get(self, request):
        name_contains = request.query_params.get('name')
        if name_contains is None:
            characters = Character.objects.all()
        else:
            characters = Character.objects.filter(name__contains=name_contains).values()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)


class CharacterCreate(APIView):
    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterRUD(APIView):
    def get_character_by_pk(self, pk):
        try:
            character = Character.objects.get(pk=pk)
        except ObjectDoesNotExist:
            character = None
        return character
    
    def get(self, request, pk):
        character = self.get_character_by_pk(pk)
        if character is None:
            return Response({'error': 'Character does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    def put(self, request, pk):
        character = self.get_character_by_pk(pk)
        if character is None:
            return Response({'error': 'Character does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        character = self.get_character_by_pk(pk)
        if character is None:
            return Response({'error': 'Character does not exist'}, status=status.HTTP_404_NOT_FOUND)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
