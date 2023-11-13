# API - Gerenciador de Tarefas

## Tecnologias utilizadas:

- Python
- Django
- Django Rest Framework
- Docker
- SQLite
- Insomnia

## Instalação e Execução da API

1 - Instale as dependências

    pip install -r requirements.txt

2 - Execute as migrações

    python manage.py makemigrations
    python manage.py migrate
    
3 - Crie um super usuário
    
    python manage.py createsuperuser
    
4 - Execute a aplicação localmente

    python manage.py runserver

5 - Endereços

    Django Admin:
  
        http://127.0.0.1:8000/admin/
        
    API:
  
        http://127.0.0.1:8000/
    
    Documentação Swagger:

        http://127.0.0.1:8000/swagger/

## Docker

Build e construção de containers:

    docker build -t api-tasks .
    docker run -p 8000:8000 api-tasks

## Especificações

- Permissão Usuario Administrador: 
    1 - Cadastrar, listar, atualizar e deletar tarefas;
    2 - Criar e deletar usuarios
- Permissão Usuario Comum:
    1 - Listar todas as tarefas disponiveis
    2 - Criar registros
