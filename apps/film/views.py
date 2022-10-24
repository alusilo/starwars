from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.film.models import Film, Director, ProductionCompany
from apps.film.serializer import FilmSerializer, DirectorSerializer, ProductionCompanySerializer

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


# Production COnpany
class ProductionCompanyListView(APIView):
    def get(self, request):
        production_companies = ProductionCompany.objects.all()
        serializer = ProductionCompanySerializer(production_companies, many=True)
        return Response(serializer.data)


class ProductionCompanyCreate(APIView):
    def post(self, request):
        serializer = ProductionCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductionCompanyRUD(APIView):
    def get_production_company_by_pk(self, pk):
        try:
            production_company = ProductionCompany.objects.get(pk=pk)
        except ObjectDoesNotExist:
            production_company = None
        return production_company
    
    def get(self, request, pk):
        production_company = self.get_production_company_by_pk(pk)
        if production_company is None:
            return Response({'error': 'Production Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductionCompanySerializer(production_company)
        return Response(serializer.data)
    
    def put(self, request, pk):
        production_company = self.get_production_company_by_pk(pk)
        if production_company is None:
            return Response({'error': 'Production Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductionCompanySerializer(production_company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        production_company = self.get_production_company_by_pk(pk)
        if production_company is None:
            return Response({'error': 'Production Company does not exist'}, status=status.HTTP_404_NOT_FOUND)
        production_company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
