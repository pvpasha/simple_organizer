from django.conf.urls import url

from . import views as accounts_views

# accounts/
urlpatterns = [

    url(r'^sing-up/$', accounts_views.RegistrationAPIView.as_view(), name='sing-up'),
    url(r'^users-list/$', accounts_views.UserListView.as_view(), name='users-list'),
    url(r'^profile/(?P<email>.+)/$', accounts_views.UserRetrieveView.as_view(), name='user-detail'),
    url(r'^profile-name/(?P<email>.+)/$', accounts_views.UserNameUpdateView.as_view(), name='user-name-update'),
    url(r'^profile-avatar/(?P<email>.+)/$', accounts_views.UserAvatarUpdateView.as_view(), name='user-avatar-update'),
    url(r'^profile-email/(?P<pk>.+)/$', accounts_views.UserEmailUpdateView.as_view(), name='user-email-update'),
    url(r'^profile-password/(?P<email>.+)/$', accounts_views.UserPasswordUpdateView.as_view(),
        name='user-password-update'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        accounts_views.activate, name='activate'),
]
