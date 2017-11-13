FROM python:3.5-onbuild

ADD . /usr/src/docker/dev_build
WORKDIR /usr/src/docker/dev_build
RUN adduser --disabled-password --gecos '' myuser
EXPOSE 80
CMD /usr/local/bin/gunicorn wsgi:application -w 2 -b :80 -t 120 --reload