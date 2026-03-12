# Star Wars Full Stack Project

Este é um projeto de estudo que implementa uma aplicação Full Stack completa para gerenciar personagens da franquia Star Wars. A aplicação consiste em uma API robusta desenvolvida com Django e um dashboard moderno construído com Vue.js e Quasar Framework.

O projeto demonstra a integração entre um back-end RESTful e um front-end reativo, incluindo funcionalidades como consumo de APIs externas (SWAPI), persistência de dados e uma interface de usuário intuitiva.

## 🚀 Funcionalidades

### Back-end (API)
- **Gerenciamento de Personagens**: CRUD completo (Create, Read, Update, Delete) de personagens.
- **Importação Automatizada**: Comando customizado para importar dados diretamente da [SWAPI (Star Wars API)](https://swapi.dev/).
- **Documentação Interativa**: API documentada com Swagger e Redoc para facilitar o consumo e testes.
- **Arquitetura Limpa**: Separação de responsabilidades utilizando ViewSets, Serializers e Services.

### Front-end (Dashboard)
- **Interface Moderna**: Desenvolvida com Quasar Framework para uma experiência de usuário fluida.
- **Listagem Reativa**: Visualização de personagens em tabelas dinâmicas.
- **Formulários Dinâmicos**: Criação e edição de personagens com validação.
- **Consumo de API**: Integração completa com o back-end utilizando Axios.

## 🛠️ Tecnologias Utilizadas

### Back-end
- **Python 3**
- **Django & Django Rest Framework**
- **SQLite3** (Banco de dados local)
- **drf-spectacular** (Documentação OpenAPI 3.0)
- **Requests** (Para integração com a SWAPI)

### Front-end
- **Vue.js 3** (Composition API)
- **Quasar Framework**
- **Vite** (Build tool rápida)
- **Axios** (Cliente HTTP)

---

## ⚙️ Configuração e Execução

### Pré-requisitos
- Python 3.10+
- Node.js 18+
- npm ou yarn

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/starwars_fullstack.git
cd starwars_fullstack
```

### 2. Back-end (Django)

1.  **Ambiente Virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Instalação e Migrações:**
    ```bash
    pip install -r requirements.txt
    cd starwars_api
    python manage.py migrate
    ```

3.  **Importar Dados Iniciais (Opcional):**
    ```bash
    python manage.py import_sw_characters
    ```

4.  **Executar Servidor:**
    ```bash
    python manage.py runserver
    ```
    Acesse em: `http://127.0.0.1:8000/`

### 3. Front-end (Quasar)

1.  **Instalação:**
    ```bash
    cd ../starwars-dashboard
    npm install
    ```

2.  **Executar Dashboard:**
    ```bash
    npm run dev
    ```
    Acesse em: `http://localhost:9000/`

---

## 📖 Documentação da API

Com o back-end rodando, você pode acessar:
- **Swagger UI:** [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)
- **Redoc:** [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- **Schema JSON:** [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)

---

## ✒️ Autor

* **Dagmar87** - [jdfssobrinho@hotmail.com](mailto:jdfssobrinho@hotmail.com)
