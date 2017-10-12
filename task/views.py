from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from accounts.models import OrganizerUser
from .models import Category, ShortTask, Task, Event
from .serializers import (CategoryListSerializer, CategorySerializer, ShortTaskListSerializer, ShortTaskSerializer,
                          TaskListSerializer, TaskSerializer, EventListSerializer, EventSerializer)


class CategoryItemView(RetrieveAPIView):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    lookup_field = 'title'


class CategoryListViewSet(ListCreateAPIView):
    queryset = Category.objects.all()          ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = CategoryListSerializer

    # def post(self, request):
    #     get_owner = request.data['owner']
    #     get_title = request.data['title']
    #     get_body = request.data['body']
    #
    #     try:
    #         user = OrganizerUser.objects.get(pk=get_owner)
    #         diary_item = Category.objects.create(owner=user, title=get_title, body=get_body)
    #         serialized_data =self.get_serializer(diary_item)
    #         return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    #     except ObjectDoesNotExist:
    #         return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class ShortTaskItemView(RetrieveAPIView):
    queryset = ShortTask.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ShortTaskSerializer
    lookup_field = 'title'


class ShortTaskListViewSet(ListCreateAPIView):
    queryset = ShortTask.objects.all()  ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = ShortTaskListSerializer


class TaskItemView(RetrieveAPIView):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer
    lookup_field = 'title'


class TaskListViewSet(ListCreateAPIView):
    queryset = Task.objects.all()  ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = TaskListSerializer

class EventItemView(RetrieveAPIView):
    queryset = Event.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    lookup_field = 'title'

class EventListViewSet(ListCreateAPIView):
    queryset = Event.objects.all()  ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = EventListSerializer


# def task(request):
#     if request.user.is_authenticated():
#         return render(request, 'task.html', {'short_task_list': ShortTask.objects.all().filter(owner=request.user),
#                                             'task_list': Task.objects.all().filter(owner=request.user),
#                                             'event_list': Event.objects.all().filter(owner=request.user),
#                                              'user_avatar': request.user.main_menu_avatar})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
#
# # def owner(request):
# #     return request.user
#
# def create_short_task(request):
#     if request.user.is_authenticated():
#         if request.method == 'POST':
#             form = ShortTaskForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/task/all/')
#         else:
#             return render(request, 'createShortTask.html', {'form': ShortTaskForm})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
#
#
# def create_task(request):
#     if request.user.is_authenticated():
#         if request.method == 'POST':
#             form = TaskForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/task/all/')
#         else:
#             return render(request, 'createTask.html', {'form': TaskForm})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
#
#
# def create_event(request):
#     if request.user.is_authenticated():
#         if request.method == 'POST':
#             form = EventForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/task/all/')
#         else: # ==>GET method
#             return render(request, 'createEvent.html', {'form': EventForm})
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))