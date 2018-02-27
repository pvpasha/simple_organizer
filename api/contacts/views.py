import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from accounts.models import OrganizerUser as User
from .serializers import ContactSerializer
from .models import Contact


logger = logging.getLogger(__name__)


class ContactsListView(ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Contact.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Object not found for user with ID #%s in contacts_list_view' % self.request.user.id)
            raise exceptions.NotFound('Object with your ID %s NotFound' % self.request.user.id)


class ContactCreateView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(pk=self.request.user.id)
                new_obj = Contact.objects.create(owner=user,
                                                 name=request.data['name'],
                                                 surname=request.data['surname'],
                                                 phone=request.data['phone'],
                                                 email_address=request.data['email_address'],
                                                 home_address=request.data['home_address'],
                                                 birthday=request.data['birthday'],
                                                 add_reminder=request.data['add_reminder'])
                serializer = self.get_serializer(new_obj)
                logger.info('Contact created with name #%s for user ID #%s in contact_create_view'
                            % (request.data['name'], self.request.user.id))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error('Data in request are wrong with user ID #%s in contact_create_view'
                             % self.request.user.id)
                raise exceptions.ValidationError('Data in request are wrong')
        except exceptions.ValidationError:
            logger.error('Can not creation contact by user ID #%s in contact_create_view' % self.request.user.id)
            raise exceptions.ValidationError('Can not creation contact. Please check your data in request')


class ContactsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return Contact.objects.filter(owner=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('Contact for user %s and ID #%s not found in contact_retrieve_update_destroy_view'
                         % (self.request.user.email, self.kwargs['pk']))
            raise exceptions.NotFound('Contact with ID #%s not found' % self.kwargs['pk'])
