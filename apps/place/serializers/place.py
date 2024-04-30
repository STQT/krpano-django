from rest_framework import serializers

from apps.place.models import Place, Property, PlaceProperty
from apps.place.serializers.category import CategorySerializer


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "icon"
        )


class PlacePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceProperty
        fields = (
            "id",
            "property",
            "value"
        )


class PlaceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    properties = PlacePropertySerializer(many=True, read_only=True)
    panos = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "slug",
            "address",
            "category",
            "phone",
            "short_description",
            "description",
            "opening_hours",
            "website",
            "telegram",
            "facebook",
            "instagram",
            "twitter",
            "youtube",
            "show_in_map",
            "is_main",
            "stars",
            "panorama",
            "video",
            "preview",
            "logo",
            "audio",
            "latitude",
            "longitude",
            "panos",
            "properties"
        )

    def get_panos(self, instance, *args, **kwargs):
        panorama = instance.panorama
        if not panorama:
            return None
        path, ext = str(panorama.url).split(".")
        pano_path = ".tiles/%s/l%l/%v/l%l_%s_%v_%h.jpg"
        request = self.context["request"]
        base_url = "{0}://{1}".format(request.scheme, request.get_host())
        return "%s%s%s" % (base_url, path, pano_path)


class PlaceListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Place
        fields = (
            "id",
            "name",
            "slug",
            "category",
            "short_description",
            "show_in_map",
            "is_main",
            "stars",
            "panorama",
            "video",
            "preview",
            "logo",
            "latitude",
            "longitude",
        )
