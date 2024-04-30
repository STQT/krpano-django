import django_filters

from apps.user.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = [
            'region',
            'is_active',
            "is_staff",
            "is_demo"
        ]