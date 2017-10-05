from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all/$', views.task),
    url(r'^create_st/$', views.create_short_task, name='add_st_task'),
    url(r'^create_task/$', views.create_task, name='add_task'),
    url(r'^create_event/$', views.create_event, name='add_event'),
]