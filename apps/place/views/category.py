from rest_framework.generics import ListAPIView

from apps.place.models import Category
from apps.place.serializers.category import CategorySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all().order_by('position')
    serializer_class = CategorySerializer
    filter_backends = []
    pagination_class = None
