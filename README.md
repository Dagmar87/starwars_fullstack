# starwars_fullstack
Projeto Full Stack de Estudo Envolvendo Star Wars

## Tecnologias Utilizadas

- Python
- Django & Django Rest Framework
- drf-spectacular (para documentação OpenAPI/Swagger)
- SQLite3 (banco de dados padrão)

## Configuração e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/starwars_fullstack.git
    cd starwars_fullstack
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Navegue até o diretório da API e execute as migrações:**
    ```bash
    cd starwars_api
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

    O servidor estará disponível em `http://127.0.0.1:8000/`.

## Endpoints da API

A documentação completa e interativa da API está disponível através do Swagger UI.

-   **Swagger UI:** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
-   **Redoc:** [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
-   **Schema (JSON):** [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)
