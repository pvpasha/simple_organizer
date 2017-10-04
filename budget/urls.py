from django.conf.urls import url, include
from . import views


urlpatterns = [


    # url(r'^organizer/', include('todo.urls')),
    # url(r'^about/$', views.about),

    url(r'^main/$', views.budget),
]