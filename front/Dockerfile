FROM tutum/nginx
RUN apt-get update
RUN service nginx upgrade
RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
CMD service nginx restart
RUN chown -R www-data /usr/src/front
RUN chmod 755 /usr/src/front
