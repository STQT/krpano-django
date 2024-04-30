from django.urls import include, path

# project
from apps.place.views import category, place

urlpatterns = [
    path("category/", category.CategoryListView.as_view()),
    path("place/", place.PlaceViewSet.as_view({"get": "list"})),
    path("place/<slug:slug>/", place.PlaceViewSet.as_view({"get": "retrieve"})),
    path(
        "place/place_place/<int:id>/",
        place.view_tour,
        name="view_tour",
    ),
]
