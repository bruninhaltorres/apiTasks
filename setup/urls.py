from django.contrib import admin
from django.urls import path, include

from tasks.views import TasksViewSet, RegistrosViewSet, CreateSuperUsuarioView
from rest_framework import routers

# Rotas principais:
router = routers.DefaultRouter()
router.register('tasks', TasksViewSet, basename='Tasks')
# router.register('usuarios', Su, basename='Create Usuarios')
router.register('registros', RegistrosViewSet, basename='Registros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', CreateSuperUsuarioView.as_view()),
    path('', include(router.urls))
]
