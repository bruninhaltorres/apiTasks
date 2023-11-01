from django.contrib import admin
from tasks.models import Task, Usuario, Registro

class Tasks(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'prioridade', 'descricao', 'data_criacao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
admin.site.register(Task, Tasks)

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
admin.site.register(Usuario, Usuarios)

class Registros(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'task', 'data_limite')
    list_display_links = ('id',)
admin.site.register(Registro, Registros)
