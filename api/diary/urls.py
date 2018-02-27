from django.conf.urls import url

from . import views as diary_views


urlpatterns = [
    url(r'^list/$', diary_views.DiaryListView.as_view(), name='diary-list'),
    url(r'^create/$', diary_views.DiaryCreateView.as_view(), name='diary-create'),
    url(r'^(?P<pk>.+)/$', diary_views.DiaryRetrieveUpdateDestroyView.as_view(), name='diary-retrieve-update-destroy')
]
