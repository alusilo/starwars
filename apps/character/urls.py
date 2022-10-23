"""starwars URL Configuration"""
from django.urls import path
from apps.character.views import CharacterListView, CharacterCreate, CharacterRUD

urlpatterns = [
    path('', CharacterCreate.as_view()),
    path('<int:pk>/', CharacterRUD.as_view()),
    path('list/', CharacterListView.as_view()),
]
