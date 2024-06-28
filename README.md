## Backend Kanastra

### Estrutura do Projeto
```bash
backend-kanastra/
├── backend_kanastra/
│   ├── settings.py
│   └── ...
├── debts/
│   └── ...
├── email_sender/
│   └── ...
├── invoice_generator/
│   └── ...
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
```

### Configuração e Execução
  #### Usando docker-compose
  - Construir e iniciar os containers
  ```bash
    docker-compose up --build
  ```
  - Parar os containers
  ```bash
    docker-compose down
  ```
  - Iniciar worker do rq
  ```bash
    docker-compose exec django python manage.py rqworker default
  ```

  #### Usando Makefile
  - Construir e iniciar os containers

  ```bash
    make up
  ```
  - Parar os containers
  ```bash
    make down
  ```
  - Para ver a lista de comandos disponíveis
  ```bash
    make help
  ```
  - Iniciar worker do rq
  ```bash
    make rq
  ```

### Dependências
  #### Requisitos
  - Docker
  - Docker Compose

