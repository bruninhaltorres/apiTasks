from django.db import models
from django.contrib.auth.models import AbstractUser

class Task(models.Model):

    PRIORIDADE = (
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baixa'),
    )
    titulo = models.CharField(max_length=15, blank=False, null=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE, blank=False, null=False, default='B')
    descricao = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class SuperUsuario(AbstractUser):

    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    is_staff = models.BooleanField(default=True)

    # Adicione related_name para evitar conflitos
    groups = models.ManyToManyField('auth.Group', related_name='usuarios')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuarios')

    def __str__(self):
        """Cada usuario sera representado pelo nome"""
        return self.nome

class AdminUsuario(models.Model):
    user = models.OneToOneField(SuperUsuario,on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.nome

class NormalUsuario(models.Model):
    user = models.OneToOneField(SuperUsuario,on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.nome

class Registro(models.Model):
    
    usuario = models.ForeignKey(NormalUsuario, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_limite = models.DateField()