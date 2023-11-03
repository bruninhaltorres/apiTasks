from django.contrib import admin
from django.urls import path, include

from tasks.views import TasksViewSet, SuperUsuarioViewSet, RegistrosViewSet
from rest_framework import routers

# Rotas principais:
router = routers.DefaultRouter()
router.register('tasks', TasksViewSet, basename='Tasks')
router.register('usuarios', SuperUsuarioViewSet, basename='Create Usuarios')
router.register('registros', RegistrosViewSet, basename='Registros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
