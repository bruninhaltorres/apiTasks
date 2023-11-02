from rest_framework import permissions

class IsAuthenticatedOrReadOnlyPermission(permissions.BasePermission):
    """Autenticação personalizada com permição somente para leitura"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Métodos seguros (GET, HEAD, OPTIONS)
            return True
        return request.user and request.user.is_authenticated