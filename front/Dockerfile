FROM tutum/nginx
RUN apt-get update
RUN service nginx upgrade
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
RUN chown -R www-data /usr/src/front
RUN chmod 755 /usr/src/front
CMD service nginx restart
