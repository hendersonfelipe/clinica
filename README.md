## Projeto de Clinica para Programação Para Internet II

No que consite este projeto:
- Administrar médicos, especialidades e agendas
- Criar uma agenda para disponibilizar as consultas
- Permitir o usuário escolher um consulta em dia e horário de acordo com agenda do médico.

## Configurando o ambiente para executar a api.
Faça o download deste repositório:
```
$ git clone git@github.com:hendersonfelipe/clinica.git
```
Crie um ambiente virtual e instale a bibliotecas disponíveis no 
arquivo requerimentes.txt

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd clinica
$ python -m venv venv
```
Depois vamos ativá-lo com o seguinte comando:

```
$ .\venv\Scripts\Activate
```

Depois de ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requeriments.txt
```

Para fazermos o primeiro acesso e poder configurar a aplicação, vamos executar o comando 
'migrate' para gerar o banco de dados padrão do Django(SQLite). E depois criar o superusuário:
```
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```

Agora devemos iniciar o servidor usando o comando:
```
(venv)$ python manage.py runserver
```

Agora vamos acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)
