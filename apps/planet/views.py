from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.planet.models import Planet
from apps.planet.serializer import PlanetSerializer

# Create your views here.
class PlanetListView(APIView):
    def get(self, request):
        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)


class PlanetCreate(APIView):
    def post(self, request):
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetRUD(APIView):
    def get_planet_by_pk(self, pk):
        try:
            planet = Planet.objects.get(pk=pk)
        except ObjectDoesNotExist:
            planet = None
        return planet
    
    def get(self, request, pk):
        planet = self.get_planet_by_pk(pk)
        if planet is None:
            return Response({'error': 'Planet does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)
    
    def put(self, request, pk):
        planet = self.get_planet_by_pk(pk)
        if planet is None:
            return Response({'error': 'Planet does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PlanetSerializer(planet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        planet = self.get_planet_by_pk(pk)
        if planet is None:
            return Response({'error': 'Planet does not exist'}, status=status.HTTP_404_NOT_FOUND)
        planet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
