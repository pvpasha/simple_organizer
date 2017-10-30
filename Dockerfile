FROM python:3.5-onbuild

ADD . /usr/src/docker/dev_build
WORKDIR /usr/src/docker/dev_build
RUN adduser --disabled-password --gecos '' myuser
EXPOSE 8000
CMD /usr/local/bin/gunicorn wsgi:application -w 2 -b :8000 -t 120 --reload