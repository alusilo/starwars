from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.film.models import Film, Director, Producer
from apps.film.serializer import FilmSerializer, DirectorSerializer, ProducerSerializer

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


# Director
class DirectorListView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)


class DirectorCreate(APIView):
    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectorRUD(APIView):
    def get_director_by_pk(self, pk):
        try:
            director = Director.objects.get(pk=pk)
        except ObjectDoesNotExist:
            director = None
        return director
    
    def get(self, request, pk):
        director = self.get_director_by_pk(pk)
        if director is None:
            return Response({'error': 'Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    
    def put(self, request, pk):
        director = self.get_director_by_pk(pk)
        if director is None:
            return Response({'error': 'Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        director = self.get_director_by_pk(pk)
        if director is None:
            return Response({'error': 'Director does not exist'}, status=status.HTTP_404_NOT_FOUND)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Producer
class ProducerListView(APIView):
    def get(self, request):
        producers = Producer.objects.all()
        serializer = ProducerSerializer(producers, many=True)
        return Response(serializer.data)


class ProducerCreate(APIView):
    def post(self, request):
        serializer = ProducerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProducerRUD(APIView):
    def get_producer_by_pk(self, pk):
        try:
            producer = Producer.objects.get(pk=pk)
        except ObjectDoesNotExist:
            producer = None
        return producer
    
    def get(self, request, pk):
        producer = self.get_producer_by_pk(pk)
        if producer is None:
            return Response({'error': 'Producer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProducerSerializer(producer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        producer = self.get_producer_by_pk(pk)
        if producer is None:
            return Response({'error': 'Producer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProducerSerializer(producer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        producer = self.get_producer_by_pk(pk)
        if producer is None:
            return Response({'error': 'Producer does not exist'}, status=status.HTTP_404_NOT_FOUND)
        producer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
