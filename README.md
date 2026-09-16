# Oficina Web

Sistema web para gerenciamento de oficinas mecânicas, desenvolvido com Django.

## Funcionalidades

- Cadastro e gerenciamento de clientes
- Cadastro e gerenciamento de veículos
- Cadastro de mecânicos
- Cadastro de fornecedores
- Controle de peças e estoque
- Cadastro de serviços
- Ordens de serviço
- Controle financeiro
- Relatórios
- Área administrativa do Django

## Tecnologias

- Python
- Django
- Django REST Framework
- SQLite
- HTML e CSS

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/diegovitor90/oficina-web.git
cd oficina-web
```

### 2. Crie e ative o ambiente virtual

No Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install django djangorestframework
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Crie um usuário administrador

```bash
python manage.py createsuperuser
```

Informe o nome de usuário, e-mail e senha quando solicitado.

### 6. Inicie o servidor

```bash
python manage.py runserver
```

Acesse o sistema em:

```text
http://127.0.0.1:8000/
```

O painel administrativo está disponível em:

```text
http://127.0.0.1:8000/admin/
```

## Rotas principais

- `/clientes/`
- `/veiculos/`
- `/mecanicos/`
- `/pecas/`
- `/servicos/`
- `/fornecedores/`
- `/estoque/`
- `/ordens-servico/`
- `/financeiro/`
- `/relatorios/`
- `/admin/`

## Executando os testes

Para executar todos os testes:

```bash
python manage.py test
```

Para testar um app específico:

```bash
python manage.py test cliente
python manage.py test mecanicos
python manage.py test veiculos
```

## Verificação do projeto

```bash
python manage.py check
```

## Estrutura do projeto

```text
oficina_web/
├── cliente/
├── core/
├── estoque/
├── financeiros/
├── fornecedores/
├── mecanicos/
├── ordens_servicos/
├── pecas/
├── relatorios/
├── servicos/
├── templates/
├── veiculos/
├── manage.py
└── README.md
```

## Observações

O banco de dados SQLite e o ambiente virtual local não devem ser enviados para o GitHub. Eles já estão configurados no arquivo `.gitignore`.

## Autor

Diego Vitor
