from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
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

    def post(self, request):
        get_owner = request.data['owner']
        get_title = request.data['title']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            category_item = Category.objects.create(owner=user, title=get_title)
            serialized_data = self.get_serializer(category_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class ShortTaskItemView(RetrieveAPIView):
    queryset = ShortTask.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ShortTaskSerializer
    lookup_field = 'title'


class ShortTaskListViewSet(ListCreateAPIView):
    queryset = ShortTask.objects.all()  ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = ShortTaskListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_title = request.data['title']
        get_body = request.data['body']
        get_category = request.data['category']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            short_task_item = ShortTask.objects.create(owner=user, title=get_title, body=get_body,
                                                       category_id=get_category)
            serialized_data = self.get_serializer(short_task_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class TaskItemView(RetrieveAPIView):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer
    lookup_field = 'title'


class TaskListViewSet(ListCreateAPIView):
    queryset = Task.objects.all()  ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = TaskListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_title = request.data['title']
        get_body = request.data['body']
        get_category = request.data['category']
        get_reminder = request.data['reminder']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            task_item = Task.objects.create(owner=user, title=get_title, body=get_body, category_id=get_category,
                                                reminder=get_reminder)
            serialized_data = self.get_serializer(task_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

class EventItemView(RetrieveAPIView):
    queryset = Event.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer
    lookup_field = 'title'

class EventListViewSet(ListCreateAPIView):
    queryset = Event.objects.all()  ## TODO: order_by(owner)
    permission_classes = (AllowAny,)
    serializer_class = EventListSerializer

    def post(self, request):
        get_owner = request.data['owner']
        get_title = request.data['title']
        get_body = request.data['body']
        get_category = request.data['category']
        get_event_date = request.data['event_date']
        try:
            user = OrganizerUser.objects.get(pk=get_owner)
            event_item = Event.objects.create(owner=user, title=get_title, body=get_body,
                                                      category_id=get_category, event_date=get_event_date)
            serialized_data = self.get_serializer(event_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

