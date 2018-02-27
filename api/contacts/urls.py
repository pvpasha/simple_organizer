from django.conf.urls import url

from . import views as contacts_views

# contacts/
urlpatterns = [
    url(r'^list/$', contacts_views.ContactsListView.as_view(), name='contact-list'),
    url(r'^create/$', contacts_views.ContactCreateView.as_view(), name='contact-create'),
    url(r'^(?P<pk>.+)/$', contacts_views.ContactsRetrieveUpdateDestroyView.as_view(),
        name='contact-retrieve-update-destroy')
]
