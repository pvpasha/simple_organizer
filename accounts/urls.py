from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views


urlpatterns = [
    url(r'^api/list-users/$', views.OrganizerUserViewSet.as_view(), name='user-list'),
    url(r'^register/$', views.RegistrationAPIView.as_view()),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
    # url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^api-auth/(?P<user_mail>.+)/$', views.OrganizerUserItemView.as_view(), name='user-detail'),
    url(r'^api/jwt-auth/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
]
