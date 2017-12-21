SHELL:=/bin/bash

build:
	docker build -t organizer .

init:
	docker run -d -p 80:80 --name organizer_1 organizer
	docker exec -it organizer_1 python manage.py makemigrations accounts diary task password budget contacts
	docker exec -it organizer_1 python manage.py migrate
	docker exec -it organizer_1 python manage.py collectstatic --noinput
bash:
	docker exec -it organizer_1 bash

stop:
	docker stop organizer_1

clear:
	docker stop organizer_1
	docker rm organizer_1
	docker rmi organizer
