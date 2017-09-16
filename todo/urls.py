from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^', views.todo),
    url(r'^2/', views.test2),
    # url(r'^articles/all/$', views.articles),
    # url(r'^articles/get/(?P<id>\d)/$', views.article),
]