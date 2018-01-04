FROM tutum/nginx
RUN apt-get update
RUN service nginx upgrade
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
CMD service nginx restart
