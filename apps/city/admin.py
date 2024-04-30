from django.contrib import admin
from parler.admin import TranslatableAdmin

from apps.city.models import City


@admin.register(City)
class CityAdmin(TranslatableAdmin):
    list_display = (
        "id",
        "name",
        "position",
        "created_at"
    )
