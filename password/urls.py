from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/$', views.PasswordOrganizerListViewSet.as_view(), name='pass-list'),
    url(r'^get/(?P<pk>.+)/$', views.PasswordOrganizerItemView.as_view(), name='pass-detail'),
]