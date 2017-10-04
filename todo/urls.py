from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^main/$', views.main),
    url(r'^about/$', views.about),
    url(r'^222/', views.test2),
]