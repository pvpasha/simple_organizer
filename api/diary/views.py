import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from accounts.models import OrganizerUser as User
from .models import Diary
from .serializers import DiarySerializer


logger = logging.getLogger(__name__)


class DiaryListView(ListAPIView):
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Diary.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in diary_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with NotFound')


class DiaryCreateView(CreateAPIView):
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Diary.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = Diary.objects.create(owner=user,
                                               title=request.data['title'],
                                               body=request.data['body'])
                serializer = self.get_serializer(new_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user #%s in diary_create_view'
                             % self.request.user.email)
                raise exceptions.ValidationError('Data in request are wrong')
        except exceptions.ValidationError:
            logger.error('Can not creation diary by user #%s in diary_create_view' % self.request.user.email)
            raise exceptions.ValidationError('Can not creation diary. Please check your data in request')


class DiaryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiarySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return Diary.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Diary for user %s and ID #%s not found in diary_retrieve_update_destroy_view'
                         % (self.request.user.email, self.kwargs['pk']))
            raise exceptions.NotFound('Diary with ID #%s not found' % self.kwargs['pk'])
