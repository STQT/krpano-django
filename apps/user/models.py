# django
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

# project import
from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("электронная почта"), unique=True, db_index=True)
    full_name = models.CharField(_("полное имя"), max_length=150, blank=True, db_index=True, null=True)
    is_staff = models.BooleanField(
        _("статус персонала"),
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        _("активный"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("дата присоединения"), default=timezone.now)
    is_demo = models.BooleanField(_("это демо"), default=False)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    class Meta:
        verbose_name = _("пользователь")
        verbose_name_plural = _("пользователи")

    def __str__(self):
        return f"{self.email}"


