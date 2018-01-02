FROM python:3.5-onbuild

ADD . /usr/src/docker/dev_build
WORKDIR /usr/src/docker/dev_build
RUN adduser --disabled-password --gecos '' myuser
CMD python manage.py runserver
