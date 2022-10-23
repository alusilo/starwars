"""starwars URL Configuration"""
from django.urls import path
from apps.film.views import FilmCreate, FilmDirectorCreate, FilmProducerCreate,\
    FilmRUD, FilmDirectorRUD, FilmProducerRUD,\
    FilmListView, FilmDirectorListView, FilmProducerListView

urlpatterns = [
    path('films/', FilmCreate.as_view()),
    path('films/<int:pk>/', FilmRUD.as_view()),
    path('films/list/', FilmListView.as_view()),
    path('films_directors/', FilmDirectorCreate.as_view()),
    path('films_directors/<int:pk>/', FilmDirectorRUD.as_view()),
    path('films_directors/list/', FilmDirectorListView.as_view()),
    path('films_producers/', FilmProducerCreate.as_view()),
    path('films_producers/<int:pk>/', FilmProducerRUD.as_view()),
    path('films_producers/list/', FilmProducerListView.as_view())
]
