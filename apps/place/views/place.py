from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.place.filters import PlaceFilter
from apps.place.models import Place
from apps.place.serializers.place import PlaceSerializer, PlaceListSerializer


class PlaceViewSet(ReadOnlyModelViewSet):
    queryset = Place.objects.filter(is_published=True)
    serializer_class = PlaceSerializer
    lookup_field = 'slug'
    filterset_class = PlaceFilter
    ordering_fields = '__all__'
    search_fields = ['translations__name']

    def get_serializer_class(self):
        if self.action == 'list':
            return PlaceListSerializer
        return self.serializer_class


@staff_member_required
def view_tour(request, id):
    print(id)
    place = Place.objects.get(id=id)
    return render(request, 'place/tour.html', {"place": place})
