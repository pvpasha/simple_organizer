import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from accounts.models import OrganizerUser as User
from .models import PasswordOrganizer
from .serializers import PasswordOrganizerSerializer


logger = logging.getLogger(__name__)


class PasswordOrganizerListView(ListAPIView):
    serializer_class = PasswordOrganizerSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return PasswordOrganizer.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in password_organizer_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with NotFound')


class PasswordOrganizerCreateView(CreateAPIView):
    serializer_class = PasswordOrganizerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = PasswordOrganizer.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = PasswordOrganizer.objects.create(owner=user,
                                                           resource_url=request.data['resource_url'],
                                                           password_res=request.data['password_res'])
                serializer = self.get_serializer(new_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user #%s in password_organizer_create_view'
                             % self.request.user.email)
                raise exceptions.ValidationError('Data in request are wrong')
        except exceptions.ValidationError:
            logger.error('Can not creation diary by user #%s in password_organizer_create_view'
                         % self.request.user.email)
            raise exceptions.ValidationError('Can not creation diary. Please check your data in request')


class PasswordOrganizerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PasswordOrganizerSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return PasswordOrganizer.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Password with ID #%s for user %s and not found in '
                         'password_organizer_retrieve_update_destroy_view'
                         % (self.kwargs['pk'], self.request.user.email))
            raise exceptions.NotFound('Password with ID #%s not found' % self.kwargs['pk'])
