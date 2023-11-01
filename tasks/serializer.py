from rest_framework import serializers
from tasks.models import Task, Usuario, Registro

class TaskSerializer(serializers.ModelSerializer):
    
    # Exibe o texto completo armazenado em prioridade e não apenas o primeiro caracter:
    prioridade = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'titulo', 'prioridade', 'descricao', 'data_criacao']

    def get_prioridade(self, obj):
        return obj.get_prioridade_display()

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):

    usuario_nome = serializers.ReadOnlyField(source = "usuario.nome")
    task_titulo = serializers.ReadOnlyField(source = "task.titulo")

    class Meta:
        model = Registro
        fields = ['id', 'task', 'task_titulo', 'usuario', 'usuario_nome', 'data_limite']