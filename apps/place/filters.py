import django_filters

from apps.place.models import Place


class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = (
            'category',
            'city',
            'is_main',
            'show_in_map'
        )
