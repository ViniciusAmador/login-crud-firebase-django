<p align="center">
  <img src="https://img.shields.io/badge/Django-3.2+-green?logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Firebase-Backend-orange?logo=firebase&logoColor=white" alt="Firebase" />
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/CRUD-Operations-blueviolet?logo=server&logoColor=white" alt="CRUD" />
  <img src="https://img.shields.io/badge/Authentication-JWT-important?logo=security&logoColor=white" alt="Authentication" />
</p>

# 🐍 Desenvolvendo Aplicações Web com Python

## Professor, Dr. Vinícius Costa Amador 

# Módulo 1
# 💻 Django Módulo 1: Tutorial de Criação de App Usuário (Login e Logout) | Django Module 1: User App Creation Tutorial (Login and Logout) | Django 模块 1：用户应用创建教程（登录和注销）

Este projeto é um guia passo a passo para criar um sistema de autenticação com Django, utilizando templates, views e testes. Ele foi iniciado em março de 2025 com Flask e FastAPI, e agora está totalmente migrado para o Django com foco em um fluxo completo de desenvolvimento.  | This project is a step-by-step guide to create an authentication system using Django, including templates, views, and testing. It was originally started in March 2025 using Flask and FastAPI, and has now been fully migrated to Django with a complete development workflow.  | 本项目是一个使用 Django 创建认证系统的逐步指南，包括模板、视图和测试。最初于 2025 年 3 月使用 Flask 和 FastAPI 启动，现在已完全迁移到 Django，专注于完整的开发流程。

---

## 🔐 Autenticação  | Authentication | 认证  

- ✅ Login funcional com `authenticate()`  | Functional login using `authenticate()`  | 使用 `authenticate()` 的功能性登录  
- 🔒 Proteção de rotas com `@login_required`  | Route protection with `@login_required`  | 使用 `@login_required` 保护路由  
- 🔁 Logout redirecionando para a página de login  | Logout redirecting to the login page  | 注销后重定向到登录页面  

---

## 🏗️ Estrutura do Projeto  | Project Structure | 项目结构  

- Projeto Django criado com `startproject`  | Django project created with `startproject`  | 使用 `startproject` 创建的 Django 项目  
- App `usuarios` criado com `startapp`  | `usuarios` app created with `startapp`  | 使用 `startapp` 创建的 `usuarios` 应用  
- Templates: `login.html` e `home.html`  | Templates: `login.html` and `home.html` | 模板：`login.html` 和 `home.html`  
- Views para login, home e logout  | Views for login, home, and logout  | 登录、主页和注销的视图  
- URLs organizadas por app  | URLs organized by app  | 按应用组织的 URL  
- Ambiente virtual (`venv`) ativo  | Virtual environment (`venv`) active  | 虚拟环境 (`venv`) 已激活  
- Superusuário criado e testado  | Superuser created and tested  | 已创建并测试超级用户  

---

## ✅ Como Rodar o Projeto  | How to Run the Project | 如何运行项目  
### Clone o repositório  | Clone the repository  | 克隆仓库  

```bash
git clone https://github.com/ViniciusAmador/login-crud-firebase-django.git
cd login_crud_firebase_project
```

### Crie e ative o ambiente virtual | Create and activate the virtual environment  | 创建并激活虚拟环境  

```bash
python -m venv venv
venv\Scriptsctivate
```

### Instale as dependências  | Install dependencies  | 安装依赖  

```bash
pip install django
```

### Migre o banco de dados  | Migrate the database  | 迁移数据库  

```bash
python manage.py migrate
```

### Crie um superusuário | Create a superuser | 创建超级用户  

```bash
python manage.py createsuperuser
```

### Rode o servidor  | Run the server  | 运行服务器  

```bash
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000`  | Access at: `http://127.0.0.1:8000`  | 访问地址：`http://127.0.0.1:8000`

---

### 🗂️ Estrutura esperada  | Expected structure  | 预期结构  

```bash
login_crud_firebase_project/
├── manage.py
├── venv/
├── meu_projeto/
│   ├── settings.py
│   ├── urls.py
├── usuarios/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── login.html
│       └── home.html
```

---

## 🧪 Testes Automatizados  | Automated Tests  | 自动化测试  

Testes criados para garantir o funcionamento de:  | Tests created to ensure:  | 创建的测试以确保：  

- Login com credenciais corretas  | Login with correct credentials  | 使用正确凭据登录 
- Falha no login com senha errada  | Login failure with incorrect password  | 使用错误密码登录失败  
- Redirecionamento correto de views protegidas  | Correct redirection of protected views  | 受保护视图的正确重定向  

Rodar os testes:  | To run the tests:  | 运行测试：

```bash
python manage.py test
```

---

## 📜 Licença  | License  | 许可证  

Este projeto está licenciado sob a licença MIT.  | This project is licensed under the MIT license.  | 本项目采用 MIT 许可证。


## ✅ PARTE 1: Criar o ambiente do projeto no VS Code  | ✅ PART 1: Create the project environment in VS Code  | ✅ 第 1 部分：在 VS Code 中创建项目环境

### 🔁 Você fará isso uma única vez no início  | 🔁 You’ll do this only once at the beginning  | 🔁 您只需在开始时执行一次

#### 1. Criar o diretório do projeto  | 1. Create the project directory  | 1. 创建项目目录

Abra o terminal no VS Code (atalho: `Ctrl +` ) e digite:  | Open the terminal in VS Code (shortcut: `Ctrl + `) and type:  | 在 VS Code 中打开终端（快捷键：`Ctrl + `），并输入：

```bash
mkdir login_crud_firebase_project
cd login_crud_firebase_project
```

#### 2. Criar e ativar o ambiente virtual  | 2. Create and activate the virtual environment  | 2. 创建并激活虚拟环境

```bash
python -m venv venv
venv\Scripts\activate
```

Ou usando o caminho completo no PowerShell:  | Or using the full path in PowerShell:  | 或使用 PowerShell 中的完整路径：

```bash
& "C:\...\Python\Python311\python.exe" -m venv venv
venv\Scripts\activate
```

#### 3. Instalar o Django  | 3. Install Django  | 3. 安装 Django

```bash
pip install django
```

## ✅ PARTE 2: Criar o projeto Django e a aplicação usuarios  | ✅ PART 2: Create the Django project and the usuarios app  | ✅ 第 2 部分：创建 Django 项目和 usuarios 应用

### 🔁 Desenvolveremos o projeto em si  | 🔁 Now we’ll build the actual project  | 🔁 我们现在将开始实际构建项目

#### Inicie o projeto  | Start the project  | 启动项目

```bash
django-admin startproject meu_projeto .
cd meu_projeto
python ../manage.py startapp usuarios
cd ..
```

#### Criar as estruturas templates/login.html e home.html  | Create the templates/login.html and home.html structure  | 创建 templates/login.html 和 home.html 的结构

##### 📁 1. Dentro da pasta usuarios/, crie uma pasta chamada templates/  | 📁 1. Inside the usuarios/ folder, create a folder named templates/  | 📁 1. 在 usuarios/ 文件夹中创建一个名为 templates/ 的文件夹

```bash
mkdir meu_projeto/usuarios/templates
```

Ou clique com o botão direito na pasta usuarios no Explorer → New Folder → nomeie como templates.  | Or right-click the usuarios folder in Explorer → New Folder → name it templates.  | 或者在资源管理器中右键点击 usuarios 文件夹 → 新建文件夹 → 命名为 templates。

##### 👉 2. Dentro da pasta templates/, crie dois arquivos:  | 👉 2. Inside the templates/ folder, create two files:  | 👉 2. 在 templates/ 文件夹中创建两个文件：

**📝 login.html** 

```html
<form method="post">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Usuário">
  <input type="password" name="password" placeholder="Senha">
  <button type="submit">Entrar</button>
</form>
```

** 📝 home.html** 

```html
<h2>Bem-vindo, {{ user.username }}!</h2>
<a href="/logout">Sair</a>
```

### 🗂️ Estrutura esperada  | Expected structure  | 预期结构  

```html
login_crud_firebase_project/
├── venv/
├── manage.py
├── meu_projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── usuarios/
│   ├── views.py
│   ├── urls.py (você irá criar)
│   ├── tests.py
│   └── templates/
│       ├── login.html
│       └── home.html

```

## ✅ PARTE 3 — Configurar o Django com o app usuarios  | ✅ PART 3 — Configure Django with the usuarios app  | ✅ 第 3 部分 — 配置 Django 使用 usuarios 应用

### 1. Registrar o app `usuarios` no `settings.py`  | 1. Register the `usuarios` app in `settings.py`  | 1. 在 `settings.py` 中注册 `usuarios` 应用

Abra o arquivo:  | Open the file:  | 打开文件：

`meu_projeto/settings.py`

Adicione 'usuarios' na lista `INSTALLED_APPS`:  | Add 'usuarios' to the `INSTALLED_APPS` list:  | 将 'usuarios' 添加到 `INSTALLED_APPS` 列表中：

```python
INSTALLED_APPS = [
    ...
    'usuarios',
]
```

### 2. Criar o arquivo de rotas `urls.py` dentro da pasta usuarios  | 2. Create the `urls.py` routes file inside usuarios folder  | 2. 在 usuarios 文件夹中创建 `urls.py` 路由文件

Crie o arquivo em: `usuarios/urls.py`  | Create the file: `usuarios/urls.py`  | 创建文件：

`usuarios/urls.py`

```python
from django.urls import path
from .views import login_view, home_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
]
```

### 3. Conectar o app ao `urls.py` principal  | 3. Connect the app to the main `urls.py`  | 3. 将应用连接到主路由文件 `urls.py`

Abra: `meu_projeto/urls.py` e inclua:  | Open: `meu_projeto/urls.py` and include:  | 打开：`meu_projeto/urls.py` 并添加：

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
]
```

### 4. Criar as views para login, home e logout  | Create the views for login, home, and logout  | 创建 login、home 和 logout 的视图函数

No arquivo: `usuarios/views.py`  | In the file: `usuarios/views.py`  | 在文件：`usuarios/views.py` 中

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
```

## 🧪 Testes Automatizados  | 🧪 Automated Tests  | 🧪 自动化测试

Testes criados para garantir o funcionamento de:  | Tests created to ensure:  | 创建的测试以确保：

- Login com credenciais corretas  | - Login with correct credentials  | - 使用正确凭据登录

- Falha no login com senha errada  | - Login failure with incorrect password  | - 使用错误密码登录失败

- Redirecionamento correto de views protegidas  | - Proper redirection of protected views  | - 正确重定向受保护视图

Rodar os testes:  | Run the tests:  | 运行测试：

```bash
python manage.py test
```

### 🎉 Pronto para rodar?  | 🎉 Ready to run?  | 🎉 准备运行了吗？

Execute os comandos finais:  | Execute the final commands:  | 执行以下命令：

- Aplicar as migrações iniciais:  | - Apply initial migrations:  | - 应用初始迁移：

```bash
python manage.py migrate
```

- Criar superusuário:  | - Create superuser:  | - 创建超级用户：

```bash
python manage.py createsuperuser
```

- Iniciar servidor local:  | - Start local server:  | - 启动本地服务器：

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000 e faça login com seu usuário.  | Access: http://127.0.0.1:8000 and log in with your user.  | 访问：http://127.0.0.1:8000 并使用您的用户登录。
