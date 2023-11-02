from rest_framework import serializers
from tasks.models import Task, Usuario, Registro

from tasks.validators import *

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'titulo', 'prioridade', 'descricao', 'data_criacao']

class UsuarioSerializer(serializers.ModelSerializer):

    is_superuser = serializers.BooleanField(label="Administrador")

    class Meta:
        model = Usuario
        fields =['id', 'nome', 'cpf', 'email', 'username', 'password', 'is_superuser', 'is_staff']

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números nesse campo"})

        return data


class RegistroSerializer(serializers.ModelSerializer):

    usuario_nome = serializers.ReadOnlyField(source = "usuario.nome")
    task_titulo = serializers.ReadOnlyField(source = "task.titulo")

    class Meta:
        model = Registro
        fields = ['id', 'task', 'task_titulo', 'usuario', 'usuario_nome', 'data_inicio', 'data_limite']

    def validate(self, data):
        if not datas_validas(data['data_inicio'], data['data_limite']):
            raise serializers.ValidationError("A data limite deve ser maior que a data de início e ambas devem ser maiores ou igual a data atual. Selecione datas válidas seguindo essa regra.")
        return data