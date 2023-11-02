from tasks.models import Task, Usuario, Registro
from tasks.serializer import TaskSerializer, UsuarioSerializer, RegistroSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    permission_classes = [IsAuthenticated]

class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
