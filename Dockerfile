FROM python:3.5-onbuild

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN apt-get install pip
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' myuser
CMD python manage.py runserver --settings=settings.base