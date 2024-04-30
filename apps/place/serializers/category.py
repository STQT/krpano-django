from rest_framework import serializers

from apps.place.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "color",
            "icon",
            "icon_svg",
        )
