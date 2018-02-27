from django.conf.urls import url

from . import views as password_org_views

# password-organizer/
urlpatterns = [
    url(r'^list/$', password_org_views.PasswordOrganizerListView.as_view(), name='password-organizer-list'),
    url(r'^create/$', password_org_views.PasswordOrganizerCreateView.as_view(), name='password-organizer-create'),
    url(r'^(?P<pk>.+)/$', password_org_views.PasswordOrganizerRetrieveUpdateDestroyView.as_view(),
        name='password-organizer-retrieve-update-destroy')
]
