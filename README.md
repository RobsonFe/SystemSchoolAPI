# Sistema de Gerenciamento de Cursos

## Descrição

Este é um sistema de gerenciamento de cursos de uma escola desenvolvido com Python utilizando Django Rest Framework (DRF) para o backend e NextJS para o frontend. O sistema persiste dados em um banco de dados relacional MySQL.

## Tecnologias Utilizadas

### Backend

- **Python**
- **Django**
- **Django Rest Framework (DRF)**
- **MySQL**

### Frontend

- **NestJS**

## Funcionalidades

- **Gerenciamento de Cursos**
  - Criação, atualização, visualização e exclusão de cursos.
- **Avaliações de Cursos**
  - Criação, atualização, visualização e exclusão de avaliações para cursos específicos.
- **Autenticação e Autorização**
  - Sistema de login e registro para usuários.
  - Diferentes níveis de permissão para usuários (admin, estudante, etc.).

## Estrutura do Projeto

### Backend

1. **Django Project Structure:**
   ```
   school/
   ├── school/
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   ├── wsgi.py
   ├── myapp/
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── serializers.py
   │   ├── urls.py
   │   ├── views.py
   ├── manage.py
   ```

### Frontend

1. **NestJS Project Structure:**
   ```
   client/
   ├── src/
   │   ├── app/
   │   ├── main.ts
   ├── package.json
   ├── tsconfig.json
   ```

## Configuração do Ambiente de Desenvolvimento

### Pré-requisitos

- **Python 3.8+**
- **Node.js 14+**
- **MySQL 8+**
- **Django 3.2+**
- **Django Rest Framework 3.12+**
- **NestJS 14+**

### Configurando o Backend

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/sistema-gerenciamento-cursos.git
   cd sistema-gerenciamento-cursos
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados no `settings.py`:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nome_do_banco_de_dados',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **Aplique as migrações:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário:**
   ```sh
   python manage.py createsuperuser
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```

### Configurando o Frontend

1. **Navegue para o diretório do cliente:**
   ```sh
   cd client
   ```

2. **Instale as dependências:**
   ```sh
   npm install
   ```

3. **Inicie o servidor de desenvolvimento:**
   ```sh
   npm run start
   ```

## Uso

### API Endpoints (Django Rest Framework)

Os endpoints da API podem ser acessados em `http://localhost:8000/api/`. Aqui estão alguns endpoints principais:

- **Cursos:**
  - `GET /api/courses/` - Lista todos os cursos
  - `POST /api/courses/` - Cria um novo curso
  - `GET /api/courses/:id/` - Detalhes de um curso específico
  - `PUT /api/courses/:id/` - Atualiza um curso específico
  - `DELETE /api/courses/:id/` - Deleta um curso específico

- **Avaliações:**
  - `GET /api/assessments/` - Lista todas as avaliações
  - `POST /api/assessments/` - Cria uma nova avaliação
  - `GET /api/assessments/:id/` - Detalhes de uma avaliação específica
  - `PUT /api/assessments/:id/` - Atualiza uma avaliação específica
  - `DELETE /api/assessments/:id/` - Deleta uma avaliação específica

# Documentação da API

## Endpoints

### Courses

#### GET /courses/
- **Descrição**: Lista todos os cursos.
- **Resposta de Sucesso**:
  - **Código**: 200 OK
  - **Corpo**:
    ```json
    [
      {
        "id": 1,
        "title": "Curso de Python",
        "url": "http://example.com/python",
        "create": "2024-06-01T00:00:00Z",
        "active": true
      }
    ]
    ```

#### POST /courses/
- **Descrição**: Cria um novo curso.
- **Corpo da Requisição**:
  - **Exemplo**:
    ```json
    {
      "title": "Curso de Django",
      "url": "http://example.com/django"
    }
    ```
- **Resposta de Sucesso**:
  - **Código**: 201 Created
  - **Corpo**:
    ```json
    {
      "id": 2,
      "title": "Curso de Django",
      "url": "http://example.com/django",
      "create": "2024-06-01T00:00:00Z",
      "active": true
    }
    ```

#### DELETE /courses/{id}/
- **Descrição**: Deleta um curso pelo ID.
- **Resposta de Sucesso**:
  - **Código**: 204 No Content

### Assessments

#### GET /assessments/
- **Descrição**: Lista todas as avaliações.
- **Resposta de Sucesso**:
  - **Código**: 200 OK
  - **Corpo**:
    ```json
    [
      {
        "id": 1,
        "course": 1,
        "name": "Robson",
        "email": "robson@example.com",
        "comment": "Ótimo curso!",
        "assessment": 5.0,
        "create": "2024-06-01T00:00:00Z",
        "active": true
      }
    ]
    ```

#### POST /assessments/
- **Descrição**: Cria uma nova avaliação.
- **Corpo da Requisição**:
  - **Exemplo**:
    ```json
    {
      "course": 1,
      "name": "Maria",
      "email": "maria@example.com",
      "comment": "Muito bom!",
      "assessment": 4.5
    }
    ```
- **Resposta de Sucesso**:
  - **Código**: 201 Created
  - **Corpo**:
    ```json
    {
      "id": 2,
      "course": 1,
      "name": "Maria",
      "email": "maria@example.com",
      "comment": "Muito bom!",
      "assessment": 4.5,
      "create": "2024-06-01T00:00:00Z",
      "active": true
    }
    ```

#### DELETE /assessments/{id}/
- **Descrição**: Deleta uma avaliação pelo ID.
- **Resposta de Sucesso**:
  - **Código**: 204 No Content


### Interface de Administração (Django Admin)

A interface de administração pode ser acessada em `http://localhost:8000/admin/`. Faça login com o superusuário que você criou anteriormente.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Autor
[Robson Ferreira](https://github.com/RobsonFe)