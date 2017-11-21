from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^api/list-users/$', views.OrganizerUserViewSet.as_view(), name='user-list'),
    url(r'^register/$', views.RegistrationAPIView.as_view(), name='registration-user'),
    url(r'^api-auth/(?P<user_mail>.+)/$', views.OrganizerUserItemView.as_view(), name='user-detail'),

]
