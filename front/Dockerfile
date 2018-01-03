FROM tutum/nginx

COPY nginx.conf /etc/nginx/nginx.conf
ADD sites-enabled/ /etc/nginx/sites-enabled/
# RUN rm /etc/nginx/sites-enabled/default
# ADD app/ /app/
EXPOSE 80
