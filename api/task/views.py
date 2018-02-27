import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from accounts.models import OrganizerUser as User
from .models import CategoryTask, ShortTask, Task, Event
from .serializers import CategoryTaskSerializer, ShortTaskSerializer, TaskSerializer,  EventSerializer


logger = logging.getLogger(__name__)


class CategoryTaskListView(ListAPIView):
    serializer_class = CategoryTaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return CategoryTask.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in category_task_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with NotFound')


class CategoryTaskCreateView(CreateAPIView):
    serializer_class = CategoryTaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CategoryTask.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = CategoryTask.objects.create(owner=user, title=request.data['title'])
                serializer = self.get_serializer(new_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user #%s in category_task_create_view'
                             % self.request.user.email)
                raise exceptions.ValidationError('Data in request are wrong')
        except exceptions.ValidationError:
            logger.error('Can not creation category task by user #%s in category_task_create_view'
                         % self.request.user.email)
            raise exceptions.ValidationError('Can not creation category task. Please check your data in request')


class CategoryTaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryTaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return CategoryTask.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Category with ID #%s for user %s not found in category_task_retrieve_update_destroy_view'
                         % (self.kwargs['pk'], self.request.user.email))
            raise exceptions.NotFound('Category with ID #%s not found' % self.kwargs['pk'])


class ShortTaskListView(ListAPIView):
    serializer_class = ShortTaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return ShortTask.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in short_task_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with NotFound')


class ShortTaskCreateView(CreateAPIView):
    serializer_class = ShortTaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ShortTask.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = ShortTask.objects.create(owner=user,
                                                   title=request.data['title'],
                                                   body=request.data['body'])
                serializer = self.get_serializer(new_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user #%s in short_task_create_view'
                             % self.request.user.email)
                raise exceptions.ValidationError('The data in request is wrong')
        except exceptions.ValidationError:
            logger.error('Can not create short task by user #%s in short_task_create_view'
                         % self.request.user.email)
            raise exceptions.ValidationError('Can not create short task. Please check your data in request')


class ShortTaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ShortTaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return ShortTask.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Short task with ID #%s for user %s and not found in short_task_retrieve_update_destroy_view'
                         % (self.kwargs['pk'], self.request.user.email))
            raise exceptions.NotFound('Short task ID #%s not found' % self.kwargs['pk'])


class TaskListView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'
# TODO: Add filter by category_task

    def get_queryset(self):
        try:
            return Task.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in task_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with NotFound')


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                category_task = CategoryTask.objects.get(pk=request.data['category'])
                new_obj = Task.objects.create(owner=user,
                                              category=category_task,
                                              title=request.data['title'],
                                              body=request.data['body'],
                                              starting_date=request.data['starting_date'],
                                              finishing_date=request.data['finishing_date'],
                                              finished=request.data['finished'],
                                              reminder_date=request.data['reminder_date'])
                serializer = self.get_serializer(new_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user #%s in task_create_view'
                             % self.request.user.email)
                raise exceptions.ValidationError('The data in request is wrong')
        except exceptions.ValidationError:
            logger.error('Can not create task by user #%s in task_create_view'
                         % self.request.user.email)
            raise exceptions.ValidationError('Can not create task. Please check your data in request')


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return Task.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Task with ID #%s for user %s not found in task_retrieve_update_destroy_view'
                         % (self.kwargs['pk'], self.request.user.email))
            raise exceptions.NotFound('Task ID #%s not found' % self.kwargs['pk'])


class EventListView(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Event.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in event_list_view' % self.request.user.email)
            raise exceptions.NotFound('Object with NotFound')


class EventCreateView(CreateAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = Event.objects.create(owner=user,
                                               title=request.data['title'],
                                               body=request.data['body'],
                                               event_date_start=request.data['event_date_start'],
                                               event_date_finish=request.data['event_date_finish'],
                                               reminder_date=request.data['reminder_date'])
                serializer = self.get_serializer(new_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user #%s in event_create_view'
                             % self.request.user.email)
                raise exceptions.ValidationError('The data in request is wrong')
        except exceptions.ValidationError:
            logger.error('Can not create event by user #%s in event_create_view'
                         % self.request.user.email)
            raise exceptions.ValidationError('Can not create event. Please check your data in request')


class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return Event.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Event with ID #%s for user %s not found in event_retrieve_update_destroy_view'
                         % (self.kwargs['pk'], self.request.user.email))
            raise exceptions.NotFound('Event ID #%s not found' % self.kwargs['pk'])
