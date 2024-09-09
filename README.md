Este projeto é uma aplicação simples em Flask com autenticação básica e configuração de firewall.

## Estrutura do Projeto
- **app.py**: Inicializa a aplicação Flask e registra as rotas.
- **routes.py**: Define as rotas principais.
- **auth.py**: Gerencia autenticação de usuários.
- **models.py**: Define o modelo de dados (usuário).
- **requirements.txt**: Dependências do projeto.

## Como Executar
1. **Clone o repositório e navegue até o diretório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
2. **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure o banco de dados:**
    No terminal Python:
    ```python
    from app import db
    db.create_all()
    ```
5. **Execute a aplicação:**
    ```bash
    python app.py
    ```
6. **Configure o Firewall (UFW):**
    ```bash
    sudo ufw enable
    sudo ufw allow 22
    sudo ufw allow 5000
    ```
7. **Acesse a aplicação:**
    No navegador, vá para `http://<IP_DO_RASPBERRY_PI>:5000`.

## Funcionalidades
- **Autenticação**: Login e logout de usuários.
- **Banco de Dados**: Gerenciamento simples com SQLite.

## Segurança
Utilize uma chave secreta adequada em produção.