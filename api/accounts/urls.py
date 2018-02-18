from django.conf.urls import url

from . import views as accounts_views


urlpatterns = [
    url(r'^sing-up/$', accounts_views.RegistrationAPIView.as_view(), name='sing_up'),
    url(r'^user-list/$', accounts_views.UserListView.as_view(), name='user_list'),
    url(r'^profile/(?P<pk>.+)/$', accounts_views.UserRetrieveUpdateView.as_view(), name='user_detail'),

]
