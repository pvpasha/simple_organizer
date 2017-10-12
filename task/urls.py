from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^cat/list/$', views.CategoryListViewSet.as_view(), name='category-list'),
    url(r'^catget/(?P<title>.+)/$', views.CategoryItemView.as_view(), name='category-detail'),
    url(r'^stask/list/$', views.ShortTaskListViewSet.as_view(), name='shorttask-list'),
    url(r'^stask/get/(?P<title>.+)/$', views.ShortTaskItemView.as_view(), name='shorttask-detail'),
    url(r'^task/list/$', views.TaskListViewSet.as_view(), name='task-list'),
    url(r'^task/get/(?P<title>.+)/$', views.TaskItemView.as_view(), name='task-detail'),
    url(r'^event/list/$', views.EventListViewSet.as_view(), name='event-list'),
    url(r'^event/get/(?P<title>.+)/$', views.EventItemView.as_view(), name='event-detail'),
]