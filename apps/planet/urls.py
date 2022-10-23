"""starwars URL Configuration"""
from django.urls import path
from apps.planet.views import PlanetListView, PlanetCreate, PlanetRUD

urlpatterns = [
    path('', PlanetCreate.as_view()),
    path('<int:pk>/', PlanetRUD.as_view()),
    path('list/', PlanetListView.as_view()),
]
