import uuid
from datetime import datetime

# django
from django.db import models
from django.contrib.gis.db.models import PointField
from django.core.validators import (
    MaxValueValidator,
    RegexValidator,
    ValidationError
)
from django.utils.translation import gettext as _

# PyPi: django-parler
from parler.models import TranslatableModel, TranslatedFields

# Project
from apps.city.models import City
from apps.core.models import BaseDateModel
from apps.core.utils import upload_media_path


def upload_panorama(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.today())[0:7]
    try:
        RegexValidator(r'^(jpg|jpeg|JPG)$').__call__(file_type)
        return 'panorama/%s/%s.%s' % (
            today, uuid.uuid4(), file_type)
    except ValidationError:
        raise ValidationError(_('Invalid file type'))


class Property(TranslatableModel, BaseDateModel):
    translations = TranslatedFields(
        name=models.CharField(_("название"), max_length=64)
    )
    icon = models.ImageField(_("икона"), upload_to=upload_media_path)

    class Meta:
        verbose_name = "Пропертй"
        verbose_name_plural = "Пропертй"

    def __str__(self):
        return self.name


class Category(TranslatableModel, BaseDateModel):
    translations = TranslatedFields(
        name=models.CharField(_("название"), max_length=64)
    )
    color = models.CharField(_("цвет"), max_length=10)
    icon = models.ImageField(_("икона"), upload_to=upload_media_path)
    icon_svg = models.ImageField(_("икона svg"), upload_to=upload_media_path)
    slug = models.SlugField(unique=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _("категория")
        verbose_name_plural = _("категории")

    def __str__(self):
        return self.name


class Place(TranslatableModel, BaseDateModel):
    translations = TranslatedFields(
        name=models.CharField(_("название"), max_length=64)
    )
    slug = models.SlugField(unique=True)
    address = models.CharField(_("адрес"), max_length=250, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="places",
        verbose_name="категория",
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        related_name='places',
        null=True,
        verbose_name="город"
    )
    phone = models.CharField(_("номер телефона"), max_length=20, blank=True, null=True)
    short_description = models.CharField(_("краткое описание"), max_length=300)
    description = models.TextField(_("описание"))
    opening_hours = models.CharField(_("часы работы"), max_length=250, null=True, blank=True)
    website = models.URLField(_("Веб-сайт"), null=True, blank=True)
    telegram = models.URLField(_("телеграм"), null=True, blank=True)
    facebook = models.URLField(_("Фейсбук"), null=True, blank=True)
    instagram = models.URLField(_("инстаграм"), null=True, blank=True)
    twitter = models.URLField(_("Твиттер"), null=True, blank=True)
    youtube = models.URLField(_("YouTube"), null=True, blank=True)
    location = PointField(_("расположение"), null=True, blank=True)
    show_in_map = models.BooleanField(_("показать на карте? "))
    is_main = models.BooleanField(_("основной"))
    is_published = models.BooleanField(_("опубликовано"))
    stars = models.PositiveSmallIntegerField(_("звезды"), default=0, validators=[MaxValueValidator(5)])

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
        verbose_name="родитель"
    )

    panorama = models.ImageField(_("панорама"), null=True, blank=True, upload_to=upload_panorama)

    video = models.FileField(_("видео"), null=True, blank=True, upload_to=upload_media_path)
    preview = models.ImageField(_("обложка"), null=True, blank=True, upload_to=upload_media_path)

    logo = models.ImageField(_("логотип"), null=True, blank=True, upload_to=upload_media_path)
    audio = models.FileField(_("аудио"), null=True, blank=True, upload_to=upload_media_path)

    class Meta:
        verbose_name = "место"
        verbose_name_plural = "места"

    def __str__(self):
        return self.name

    @property
    def latitude(self):
        return self.location.x if self.location else None

    @property
    def longitude(self):
        return self.location.y if self.location else None


class PlaceProperty(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="properties", verbose_name="место")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="properties", verbose_name="пропертй")
    value = models.CharField(_("валуе"))

    class Meta:
        verbose_name = "место пропертй"
        verbose_name_plural = "место пропертй"


