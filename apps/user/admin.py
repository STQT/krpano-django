from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from apps.user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id", "email", "full_name", "is_active", "is_superuser", "date_joined",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "full_name",
                    "password",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "full_name",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("email", "full_name")
    ordering = ("-date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_filter = ("is_staff", "is_superuser")
