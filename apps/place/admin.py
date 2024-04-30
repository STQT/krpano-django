from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.translation import gettext as _
from parler.admin import TranslatableAdmin

from apps.core import krpano
from apps.place.models import Place, Category, Property, PlaceProperty


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return '-'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = (
        "id",
        "name",
        "color",
        "slug",
        "created_at"
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'slug',
                'color',
                'icon',
                'icon_svg',
                'position'
            ),
        }),
    )

    search_fields = [
        "translations__name"
    ]

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }


@admin.register(Property)
class PropertyAdmin(TranslatableAdmin):
    list_display = (
        "id",
        "name",
        "created_at"
    )


class PlacePropertyInlineAdmin(admin.StackedInline):
    model = PlaceProperty
    list_display = (
        "id",
        "place",
    )
    extra = 1


@admin.register(Place)
class PlaceAdmin(TranslatableAdmin):
    list_display = (
        "id",
        "name",
        linkify(field_name="category"),
        linkify(field_name="city"),
        "is_published",
        "is_main",
        "created_at",
        "view_tour"

    )
    list_filter = [
        "city",
        "category",
        "is_main",
        "is_published",
        "show_in_map",
        "created_at",
    ]
    list_select_related = ['category', 'city']
    inlines = [PlacePropertyInlineAdmin]
    search_fields = [
        "translations__name"
    ]
    fieldsets = (
        (None, {
            'fields': (
                'parent',
                'name',
                'slug',
                'category',
                'city',
                'address',
                'phone',
                'opening_hours',
                'stars',
                'short_description',
                'description',
                'location',
            ),
        }),
        (_("Ссылки"), {
            'fields': (
                'website',
                'telegram',
                'facebook',
                'instagram',
                'twitter',
                'youtube',
            ),
        }),
        (_("логические поля"), {
            'fields': (
                'show_in_map',
                'is_main',
                'is_published',
            ),
        }),
        (_("Медиа"), {
            'fields': (
                'panorama',
                'video',
                'preview',
                'logo',
                'audio'
            ),
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }

    def save_model(self, request, obj, form, change):
        old_panorama = form.initial.get("panorama")
        old_panorama_url = None
        if old_panorama:
            old_panorama_url = old_panorama.url
        super().save_model(request, obj, form, change)
        if 'panorama' in form.changed_data:
            new_panorama_url = obj.panorama.url
            krpano.tile_full(new_panorama_url, old_panorama_url)

    def view_tour(self, obj):
        url = reverse("view_tour", args=[obj.id])
        return mark_safe(f'<a href="{url}" class="button">{_("Смотреть")}</a>')

    view_tour.short_description = _("вид 360")
    view_tour.allow_tags = True
