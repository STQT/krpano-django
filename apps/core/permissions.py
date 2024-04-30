from rest_framework.permissions import BasePermission

from apps.user.models import User


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.user_type
            == User.CUSTOMER
        )


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        base_permission = bool(
            request.user
            and request.user.is_authenticated
            and request.user.user_type
            == User.VENDOR
        )
        return base_permission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        base_permission = bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
            == User.ADMIN
        )
        return base_permission
