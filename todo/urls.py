from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^main/$', views.main),
    url(r'^about/$', views.about),
]
