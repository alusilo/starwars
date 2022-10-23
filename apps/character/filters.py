from django_filters import FilterSet
from apps.character.models import Character


class CharacterFilter(FilterSet):
    class Meta:
        model = Character
        fields = {
            'name': ['exact', 'contains'],
        }
