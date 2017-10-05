from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all/$', views.contacts),
    url(r'^create_contact/$', views.create_contact, name='add_contact'),
]