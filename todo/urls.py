from django.conf.urls import url
from . import views




urlpatterns = [
    url(r'^main/$', views.main),
    url(r'^todo/', views.todo),
    url(r'^task/$', views.task),
    url(r'^event/$', views.event),
    url(r'^diary/$', views.diary),
    url(r'^budget/$', views.budget),
    url(r'^contact/$', views.contact),
    url(r'^passorg/$', views.passorg),
    url(r'^about/$', views.about),

    url(r'^222/', views.test2),
    # url(r'^articles/all/$', views.articles),
    # url(r'^articles/get/(?P<id>\d)/$', views.article),
]