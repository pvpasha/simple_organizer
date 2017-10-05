from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all/$', views.passorg),
    url(r'^create_passw/$', views.create_passw, name='create_passw')
]