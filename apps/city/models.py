from django.contrib.gis.db.models import PointField
from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatedFields, TranslatableModel

from apps.core.models import BaseDateModel


class City(TranslatableModel, BaseDateModel):
    translations = TranslatedFields(
        name=models.CharField(_("название"), max_length=64)
    )
    location = PointField(_("расположение"), geography=True)
    position = models.PositiveSmallIntegerField(_("позиция"))

    class Meta:
        verbose_name = "город"
        verbose_name_plural = "города"

    def __str__(self):
        return self.name

    @property
    def latitude(self):
        return self.location.x if self.location else None

    @property
    def longitude(self):
        return self.location.y if self.location else None
