SHELL:=/bin/bash

build:
	docker-compose build

up:
	docker-compose up -d

init:
	docker-compose up -d
	docker exec -it api_1 python manage.py makemigrations accounts diary task password budget contacts
	docker exec -it api_1 python manage.py migrate
	docker exec -it api_1 python manage.py collectstatic --noinput
	docker-compose stop

bash:
	docker exec -it organizer_1 bash

stop:
	docker-compose stop

clear:
	docker stop api_1
	docker stop postgres_1
	docker rm api_1
	docker rm postgres_1
	docker rmi api
	docker rmi postgres
