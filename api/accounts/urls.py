from django.conf.urls import url
from django.views.generic import TemplateView

from . import views as accounts_views


urlpatterns = [
    url(r'^register/$', accounts_views.RegistrationAPIView.as_view(), name='registration-user'),
    url(r'^api/list-users/$', accounts_views.OrganizerUserViewSet.as_view(), name='user-list'),
    url(r'^api/(?P<email>.+)/$', accounts_views.OrganizerUserItemView.as_view(), name='user-detail'),
    url(r'^api-login/$', accounts_views.LoginAPIView.as_view(), name='api-login'),

    url(r'^login-error/$', TemplateView.as_view(template_name='login-error.html'), name='login-error'),
]
