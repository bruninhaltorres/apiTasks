from django.contrib import admin
from django.urls import path, include

from tasks.views import TasksViewSet, SuperUsuarioViewSet, RegistrosViewSet
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Recursos",
        default_version='v1',
        description="Gerenciamento de Recursos",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Rotas principais:
router = routers.DefaultRouter()
router.register('tasks', TasksViewSet, basename='Tasks')
router.register('usuarios', SuperUsuarioViewSet, basename='Create Usuarios')
router.register('registros', RegistrosViewSet, basename='Registros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls))
] 
