from rest_framework import permissions

class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsNormalPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user
    
class IsReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Métodos seguros (GET, HEAD, OPTIONS)
            return True
        return request.user and request.user.is_admin