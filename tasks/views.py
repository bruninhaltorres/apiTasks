from rest_framework import viewsets

from tasks.models import Task, SuperUsuario, Registro
from tasks.permissions import *
from tasks.serializer import TaskSerializer, SuperUsuarioSerializer, RegistroSerializer

from rest_framework.permissions import IsAuthenticated

class TasksViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated&IsReadOnly]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SuperUsuarioViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated&IsAdminPermission]

    queryset = SuperUsuario.objects.all()
    serializer_class = SuperUsuarioSerializer

class RegistrosViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated&IsNormalPermission]

    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
