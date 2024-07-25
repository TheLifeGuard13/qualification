import typing

from rest_framework import permissions


class IsActiveStaff(permissions.BasePermission):
    """Проверяет является ли сотрудник активным."""

    def has_permission(self, request: typing.Any, view: typing.Any) -> bool:
        if request.user.is_active and request.user.is_staff:
            return True
        return False
