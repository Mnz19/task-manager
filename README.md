# 🧱 TaskManager - Sistema de Gestão de Tarefas com SOLID e Django

TaskManager é uma aplicação back-end desenvolvida com Django, com foco na aplicação dos princípios SOLID. O sistema permite que equipes colaborem em tarefas, atribuam responsabilidades, acompanhem prazos e mantenham um histórico de alterações — tudo com uma arquitetura limpa e escalável.

## 🚀 Objetivos do Projeto

- Treinar os princípios do SOLID na prática
- Utilizar uma arquitetura orientada a serviços (Service Layer)
- Organizar um projeto Django de forma modular e escalável
- Facilitar a leitura, manutenção e testes do código

---

## 🧩 Funcionalidades

- 📋 Cadastro e autenticação de usuários
- 👥 Criação e gestão de equipes
- ✅ Criação, atualização e finalização de tarefas
- 🔄 Atribuição de tarefas a membros da equipe
- 🗂️ Organização de tarefas por prioridade, status e prazo
- 🕒 Histórico de alterações nas tarefas
- 🔔 Notificações básicas sobre mudanças importantes

---

## 🛠️ Tecnologias utilizadas

- [Python 3.12+](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/) (ou SQLite para testes locais)

---

## 🧱 Princípios SOLID aplicados

- **S – Single Responsibility Principle:** cada classe (models, views, services) possui uma única responsabilidade clara.
- **O – Open/Closed Principle:** arquitetura preparada para extensão sem modificação do núcleo.
- **L – Liskov Substitution Principle:** uso de heranças e interfaces respeitando contratos.
- **I – Interface Segregation Principle:** uso de abstrações focadas para cada responsabilidade.
- **D – Dependency Inversion Principle:** lógica de negócio desacoplada da infraestrutura, por meio de serviços.

---

## 🔧 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seuusuario/taskmanager-solid-django.git
cd taskmanager-solid-django

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows use `venv\Scripts\activate`

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
