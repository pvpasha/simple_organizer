from django.conf.urls import url

from . import views


urlpatterns = [
    # url(r'^all/$', views.contacts),
    # url(r'^create_contact/$', views.create_contact, name='add_contact'),
    url(r'^list/$', views.ContactListViewSet.as_view(), name='contact-list'),
    url(r'^get/(?P<pk>.+)/$', views.ContactItemView.as_view(), name='contact-detail'),
]