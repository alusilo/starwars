from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.film.models import Film, FilmDirector, FilmProducer, FilmPlanet
from apps.film.serializer import FilmSerializer, FilmDirectorSerializer, FilmProducerSerializer, FilmPlanetSerializer

# Create your views here.
# Film
class FilmListView(APIView):
    def get(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)


class FilmCreate(APIView):
    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmRUD(APIView):
    def get_film_by_pk(self, pk):
        try:
            film = Film.objects.get(pk=pk)
        except ObjectDoesNotExist:
            film = None
        return film
    
    def get(self, request, pk):
        film = self.get_film_by_pk(pk)
        if film is None:
            return Response({'error': 'Film does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmSerializer(film)
        return Response(serializer.data)
    
    def put(self, request, pk):
        film = self.get_film_by_pk(pk)
        if film is None:
            return Response({'error': 'Film does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        film = self.get_film_by_pk(pk)
        if film is None:
            return Response({'error': 'Film does not exist'}, status=status.HTTP_404_NOT_FOUND)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FilmDirector
class FilmDirectorListView(APIView):
    def get(self, request):
        films_directors = FilmDirector.objects.all()
        serializer = FilmDirectorSerializer(films_directors, many=True)
        return Response(serializer.data)


class FilmDirectorCreate(APIView):
    def post(self, request):
        serializer = FilmDirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDirectorRUD(APIView):
    def get_film_director_by_pk(self, pk):
        try:
            film_director = FilmDirector.objects.get(pk=pk)
        except ObjectDoesNotExist:
            film_director = None
        return film_director
    
    def get(self, request, pk):
        film_director = self.get_film_director_by_pk(pk)
        if film_director is None:
            return Response({'error': 'Film Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmDirectorSerializer(film_director)
        return Response(serializer.data)
    
    def put(self, request, pk):
        film_director = self.get_film_director_by_pk(pk)
        if film_director is None:
            return Response({'error': 'Film Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmDirectorSerializer(film_director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        film_director = self.get_film_director_by_pk(pk)
        if film_director is None:
            return Response({'error': 'Film Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
        film_director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FilmProducer
class FilmProducerListView(APIView):
    def get(self, request):
        films_producers = FilmProducer.objects.all()
        serializer = FilmProducerSerializer(films_producers, many=True)
        return Response(serializer.data)


class FilmProducerCreate(APIView):
    def post(self, request):
        serializer = FilmProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmProducerRUD(APIView):
    def get_film_producer_by_pk(self, pk):
        try:
            film_producer = FilmProducer.objects.get(pk=pk)
        except ObjectDoesNotExist:
            film_producer = None
        return film_producer
    
    def get(self, request, pk):
        film_producer = self.get_film_producer_by_pk(pk)
        if film_producer is None:
            return Response({'error': 'Film Producer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmProducerSerializer(film_producer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        film_producer = self.get_film_producer_by_pk(pk)
        if film_producer is None:
            return Response({'error': 'Film Producer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmProducerSerializer(film_producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        film_producer = self.get_film_producer_by_pk(pk)
        if film_producer is None:
            return Response({'error': 'Film Producer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        film_producer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FilmPlanet
class FilmPlanetListView(APIView):
    def get(self, request):
        films_planets = FilmPlanet.objects.all()
        serializer = FilmPlanetSerializer(films_planets, many=True)
        return Response(serializer.data)


class FilmPlanetCreate(APIView):
    def post(self, request):
        serializer = FilmPlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmPlanetRUD(APIView):
    def get_film_planet_by_pk(self, pk):
        try:
            film_planet = FilmPlanet.objects.get(pk=pk)
        except ObjectDoesNotExist:
            film_planet = None
        return film_planet
    
    def get(self, request, pk):
        film_planet = self.get_film_planet_by_pk(pk)
        if film_planet is None:
            return Response({'error': 'Film Planet does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmPlanetSerializer(film_planet)
        return Response(serializer.data)
    
    def put(self, request, pk):
        film_planet = self.get_film_planet_by_pk(pk)
        if film_planet is None:
            return Response({'error': 'Film Planet does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FilmPlanetSerializer(film_planet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        film_planet = self.get_film_planet_by_pk(pk)
        if film_planet is None:
            return Response({'error': 'Film Planet does not exist'}, status=status.HTTP_404_NOT_FOUND)
        film_planet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
