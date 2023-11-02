from tasks.models import Task, SuperUsuario, AdminUsuario, NormalUsuario, Registro
from tasks.serializer import TaskSerializer, CreateSuperUsuarioSerializer, RegistroSerializer
from rest_framework import viewsets, generics

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateSuperUsuarioView(generics.GenericAPIView):
    # queryset = Task.objects.all()
    serializer_class = CreateSuperUsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"account created successfully"
        })


class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
