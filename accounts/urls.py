from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/$', views.OrganizerUserViewSet.as_view(), name='user-list'),
    url(r'^user/(?P<user_mail>.+)/$', views.OrganizerUserItemView.as_view(), name='user-detail'),
]