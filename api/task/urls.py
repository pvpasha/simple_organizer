from django.conf.urls import url

from . import views as task_views

# task/
urlpatterns = [
    url(r'^category-list/$', task_views.CategoryTaskListView.as_view(), name='category-task-list'),
    url(r'^category-create/$', task_views.CategoryTaskCreateView.as_view(), name='category-task-create'),
    url(r'^category-(?P<pk>.+)/$', task_views.CategoryTaskRetrieveUpdateDestroyView.as_view(),
        name='category-task-retrieve-update-destroy'),
    url(r'^short-list/$', task_views.ShortTaskListView.as_view(), name='short-task-list'),
    url(r'^short-create/$', task_views.ShortTaskCreateView.as_view(), name='short-task-create'),
    url(r'^short-(?P<pk>.+)/$', task_views.ShortTaskRetrieveUpdateDestroyView.as_view(),
        name='short-task-retrieve-update-destroy'),
    url(r'^list/$', task_views.TaskListView.as_view(), name='task-list'),
    url(r'^create/$', task_views.TaskCreateView.as_view(), name='task-create'),
    url(r'^(?P<pk>.+)/$', task_views.TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    url(r'^event-list/$', task_views.EventListView.as_view(), name='event-list'),
    url(r'^event-create/$', task_views.EventCreateView.as_view(), name='event-create'),
    url(r'^event-(?P<pk>.+)/$', task_views.EventRetrieveUpdateDestroyView.as_view(),
        name='event-retrieve-update-destroy')
]
