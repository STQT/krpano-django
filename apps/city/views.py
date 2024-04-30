from rest_framework.generics import ListAPIView

from apps.city.models import City
from apps.city.serializers import CitySerializer


class CityListView(ListAPIView):
    queryset = City.objects.all().order_by('position')
    serializer_class = CitySerializer
    pagination_class = None
    filter_backends = []
