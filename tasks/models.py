from django.db import models

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

class Usuario(models.Model):

    nome = models.CharField(max_length=30, blank=False, null=False)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        """Cada usuario sera representado pelo nome"""
        return self.nome
    
class Registro(models.Model):
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    data_limite = models.DateField()