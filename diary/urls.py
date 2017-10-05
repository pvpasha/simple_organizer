from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all/$', views.diary),
    url(r'^create_diary/$', views.create_diary, name='add_diary'),
]