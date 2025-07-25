from  rest_framework import permissions

class IsAdminOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return bool(request.user and request.user.is_staff)

