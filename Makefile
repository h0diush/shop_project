ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env_dev
endif

migrate:
	docker-compose exec web python manage.py migrate


static:
	docker-compose exec web python manage.py collectstatic --no-input

run:
	docker-compose -f docker-compose.dev.yml up -d --build

stop:
	docker-compose -f docker-compose.dev.yml down -v

restart_nginx:
	docker-compose restart nginx

nginx_bash:
	docker-compose exec nginx bash


superuser:
	docker-compose exec web python manage.py createsuperuser

data:
	docker-compose exec web python manage.py loaddata data.json
