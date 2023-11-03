from rest_framework import permissions

class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsNormalPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user