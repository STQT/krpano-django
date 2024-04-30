from django.urls import path

# project
from apps.city.views import CityListView

urlpatterns = [
    path("city/", CityListView.as_view())
]
