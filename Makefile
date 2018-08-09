SHELL:=/bin/bash

build:
	docker-compose build

up:
	docker-compose up -d

init:
	docker-compose up -d
	docker exec -it devbuild_api_1 python manage.py makemigrations accounts diary task password budget contacts thumbnail
	docker exec -it devbuild_api_1 python manage.py migrate
	docker exec -it devbuild_api_1 python manage.py collectstatic --noinput
	docker-compose stop

bash-api:
	docker exec -it devbuild_api_1 bash

bash-front:
	docker exec -it devbuild_front_1 bash

bash-postgres:
	docker exec -it devbuild_postgres_1 bash

stop:
	docker-compose stop

stop-api:
	docker stop devbuild_api_1

stop-postgres:
	docker stop devbuild_postgres_1

stop-front:
	docker stop devbuild_front_1

clear:
	docker stop devbuild_api_1
	docker stop devbuild_postgres_1
	docker stop devbuild_front_1
	docker rm devbuild_api_1
	docker rm devbuild_postgres_1
	docker rm devbuild_front_1
	docker rmi devbuild_api
	docker rmi postgres
	docker rmi devbuild_front
