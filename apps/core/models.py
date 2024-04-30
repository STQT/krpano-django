from django.db import models
from django.utils.translation import gettext as _


class BaseDateModel(models.Model):
    created_at = models.DateTimeField(_("создано"), auto_now_add=True)
    updated_at = models.DateTimeField(_("обновленное время"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)

    def has_changes(self, **kwargs):
        a = any(getattr(self, k) != v for k, v in kwargs.items())
        return a

    def save_changes_if_has(self, **kwargs):
        if self.has_changes(**kwargs):
            for field, value in kwargs.items():
                setattr(self, field, value)
            self.save()


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
