COMPOSE_FILE := docker-compose.yaml
include .env


build:
	docker compose -f $(COMPOSE_FILE) build

up:
	docker compose -f $(COMPOSE_FILE) up

down:
	docker compose -f $(COMPOSE_FILE) down

loc: build up

exec:
	docker compose -f $(COMPOSE_FILE) exec api bash

makemigrations:
	docker compose -f $(COMPOSE_FILE) exec -it api bash -c "python manage.py makemigrations"

migrate:
	docker compose -f $(COMPOSE_FILE) exec -it api bash -c "python manage.py migrate"

test:
	docker compose -f $(COMPOSE_FILE) exec -it api bash -c "python manage.py test"
