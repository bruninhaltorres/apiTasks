from tasks.models import Task, Usuario, Registro
from tasks.serializer import TaskSerializer, UsuarioSerializer, RegistroSerializer
from rest_framework import viewsets

from tasks.permissions import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticatedOrReadOnlyPermission]

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
