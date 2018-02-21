from django.conf.urls import url

from . import views as accounts_views


urlpatterns = [
    url(r'^sing-up/$', accounts_views.RegistrationAPIView.as_view(), name='sing_up'),
    url(r'^users-list/$', accounts_views.UserListView.as_view(), name='users_list'),

    url(r'^profile/(?P<email>.+)/$', accounts_views.UserRetrieveView.as_view(), name='user_detail'),
    url(r'^profile-name/(?P<email>.+)/$', accounts_views.UserNameUpdateView.as_view(), name='user_name_update'),
    url(r'^profile-avatar/(?P<email>.+)/$', accounts_views.UserAvatarUpdateView, name='user_avatar_update'),
    url(r'^profile-email/(?P<pk>.+)/$', accounts_views.UserEmailUpdateView.as_view(), name='user_email_update'),
    url(r'^profile-password/(?P<email>.+)/$', accounts_views.UserPasswordUpdateView.as_view(), name='user_password_update'),

]
