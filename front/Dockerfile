FROM tutum/nginx
RUN apt-get update
RUN service nginx upgrade
RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
RUN mkdir /usr/src/front
ADD . /usr/src/front
WORKDIR /usr/src/front
CMD service nginx restart
