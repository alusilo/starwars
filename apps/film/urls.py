"""starwars URL Configuration"""
from django.urls import path
from apps.film.views import FilmCreate, DirectorCreate, ProductionCompanyCreate,\
    FilmRUD, DirectorRUD, ProductionCompanyRUD,\
    FilmListView, DirectorListView, ProductionCompanyListView

urlpatterns = [
    path('films/', FilmCreate.as_view()),
    path('films/<int:pk>/', FilmRUD.as_view()),
    path('films/list/', FilmListView.as_view()),
    path('films_directors/', DirectorCreate.as_view()),
    path('films_directors/<int:pk>/', DirectorRUD.as_view()),
    path('films_directors/list/', DirectorListView.as_view()),
    path('production_companies/', ProductionCompanyCreate.as_view()),
    path('production_companies/<int:pk>/', ProductionCompanyRUD.as_view()),
    path('production_companies/list/', ProductionCompanyListView.as_view())
]
