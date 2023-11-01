from tasks.models import Task, Usuario, Registro
from tasks.serializer import TaskSerializer, UsuarioSerializer, RegistroSerializer

from rest_framework import viewsets

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer