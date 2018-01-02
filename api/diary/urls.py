from django.conf.urls import url
from rest_framework import routers

from . import views


# router = routers.SimpleRouter()
# router.register(r'diary', views.DiaryListViewSet, base_name='diary_list')
# urlpatterns = router.urls

urlpatterns = [
    url(r'^$', views.DiaryListViewSet.as_view()),
    url(r'^get/(?P<title>.+)/$', views.DiaryItemView.as_view(), name='diary-detail'),
    # url(r'^create_diary/$', views.create_diary, name='add_diary'),
]