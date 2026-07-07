from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to only allow superusers to access certain views.
    """

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True  # Allow other methods for all users
        # return request.user and request.user.is_superuser