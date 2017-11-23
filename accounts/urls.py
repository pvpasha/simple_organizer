from django.conf.urls import url

from . import views as accounts_views


urlpatterns = [
    url(r'^api/list-users/$', accounts_views.OrganizerUserViewSet.as_view(), name='user-list'),
    url(r'^register/$', accounts_views.RegistrationAPIView.as_view(), name='registration-user'),
    url(r'^api-auth/(?P<user_mail>.+)/$', accounts_views.OrganizerUserItemView.as_view(), name='user-detail'),
    url(r'^settings/', accounts_views.SettingsSocialAuth, name='settings-social-auth'),

]
