DOCKER_COMPOSE = docker-compose
PROJECT_NAME = backend-kanastra

build:
	@$(DOCKER_COMPOSE) build

up:
	@$(DOCKER_COMPOSE) up -d --remove-orphans

down:
	@$(DOCKER_COMPOSE) down --remove-orphans

migrate:
	@$(DOCKER_COMPOSE) run django python manage.py migrate

makemigrations:
	@$(DOCKER_COMPOSE) run django python manage.py makemigrations

createsuperuser:
	@$(DOCKER_COMPOSE) run django python manage.py createsuperuser

shell:
	@$(DOCKER_COMPOSE) run django python manage.py shell

collectstatic:
	@$(DOCKER_COMPOSE) run django python manage.py collectstatic --noinput

logs:
	@$(DOCKER_COMPOSE) logs -f --tail 200 django

test:
	@$(DOCKER_COMPOSE) run django python manage.py test

install:
	@$(DOCKER_COMPOSE) run django pip install -r requirements.txt

rebuild:
	@$(DOCKER_COMPOSE) down --rmi all
	@$(DOCKER_COMPOSE) build --no-cache --force-rm

restart:
	@$(DOCKER_COMPOSE) restart

start_rq_worker:
	@$(DOCKER_COMPOSE) run django python manage.py rqworker default

help:
	@echo "Comandos:"
	@echo "  build            - Construir as imagens Docker"
	@echo "  up               - Iniciar os containers Docker"
	@echo "  down             - Parar os containers Docker"
	@echo "  migrate          - Executar migrações do Django"
	@echo "  makemigrations   - Criar migrações do Django"
	@echo "  createsuperuser  - Criar superusuário do Django"
	@echo "  shell            - Abrir o shell do Django"
	@echo "  collectstatic    - Coletar arquivos estáticos do Django"
	@echo "  logs             - Ver logs dos containers"
	@echo "  test             - Executar testes do Django"
	@echo "  install          - Instalar dependências do projeto"
	@echo "  rebuild          - Rebuild das imagens Docker"
	@echo "  help             - Mostrar esta mensagem de ajuda"
