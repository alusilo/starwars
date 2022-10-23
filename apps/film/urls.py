"""starwars URL Configuration"""
from django.urls import path
from apps.film.views import FilmCreate, DirectorCreate, ProducerCreate,\
    FilmRUD, DirectorRUD, ProducerRUD,\
    FilmListView, DirectorListView, ProducerListView

urlpatterns = [
    path('films/', FilmCreate.as_view()),
    path('films/<int:pk>/', FilmRUD.as_view()),
    path('films/list/', FilmListView.as_view()),
    path('directors/', DirectorCreate.as_view()),
    path('directors/<int:pk>/', DirectorRUD.as_view()),
    path('directors/list/', DirectorListView.as_view()),
    path('producers/', ProducerCreate.as_view()),
    path('producers/<int:pk>/', ProducerRUD.as_view()),
    path('producers/list/', ProducerListView.as_view())
]
