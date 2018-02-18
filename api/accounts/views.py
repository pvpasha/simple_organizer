import logging

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView

from .models import OrganizerUser
from .serializers import OrganizerUserListSerializer, OrganizerUserSerializer


logger = logging.getLogger(__name__)


class RegistrationAPIView(CreateAPIView):           # >> sing-up/
    permission_classes = (AllowAny,)
    serializer_class = OrganizerUserSerializer
    queryset = OrganizerUser.objects.all()

    def post(self, request, *args, **kwargs):
        user_data = request.data
        if user_data['password1'] == user_data['password2']:
            user = OrganizerUser.objects.create_user(email=user_data['email'],
                                                     username=user_data['username'],
                                                     password=user_data['password1'])
            serializer = self.get_serializer_class()
            logger.info('User with email: "%s" and name: "%s" was created successful.' % (
                user_data['email'], user_data['username']))
            return Response(serializer(user).data, status=status.HTTP_201_CREATED)
        else:
            logger.error('Can not create user with email: "%s" and name: "%s". Passwords does not match.' % (
                user_data['email'], user_data['username']))
            return ValidationError('Cannot create. Passwords does not match.', code=status.HTTP_417_EXPECTATION_FAILED)


class UserListView(ListAPIView):            # >> user-list/
    # queryset = OrganizerUser.objects.all()
    permission_classes = (AllowAny,)                # must will change to 'permissions.IsAdminUser'
    serializer_class = OrganizerUserListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            user_inst = OrganizerUser.objects.get(pk=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('User with ID %s does not exist' % self.request.user.id)
            raise exceptions.NotFound('Cant get user with ID %s for user_list_view' % self.request.user.id)
        if user_inst.is_staff:
            return OrganizerUser.objects.only('id', 'email', 'username', 'second_name')
        else:
            logger.error('User with ID %s have no permissions to users instances' % self.request.user.id)
            raise exceptions.PermissionDenied('User with ID %s have no permissions to users instances' % self.request.user.id)



    # def list(self, request, *args, **kwargs):
    #     user_inst = OrganizerUser.objects.get(pk=self.request.user.id)
    #     if user_inst.is_staff:
    #         users_list = self.queryset
    #         response = []
    #         for user in users_list:
    #             u = {}
    #             u['user_name'] = user.username
    #             u['second_name'] = user.second_name
    #             response.append(u)
    #         return Response(response, status=status.HTTP_200_OK)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):       # >> user-email/
    permission_classes = (AllowAny,)                # must will change to 'IsAuthenticated'
    serializer_class = OrganizerUserListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            if self.request.user.id == int(self.kwargs['pk']):
                return OrganizerUser.objects.only('id', 'email', 'username', 'second_name')
            else:
                logger.error('User with ID %s cannot get user instance with ID %s' % (self.request.user.id, self.kwargs['pk']))
                raise exceptions.PermissionDenied('Cant get user with ID %s for user_retrieve_view' % self.kwargs['pk'])
        except ObjectDoesNotExist:
            logger.error('User with ID %s does not exist' % self.request.user.id)
            raise exceptions.NotFound('Cant get user with ID %s for user_retrieve_view' % self.request.user.id)

#
# class UserUpdateView(UpdateAPIView):       # >> user-email/update/
#     queryset = OrganizerUser.objects.only('id', 'email', 'username', 'second_name')
#     permission_classes = (AllowAny,)                # must will change to 'IsAuthenticated'
#     serializer_class = OrganizerUserListSerializer
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         try:
#             if self.request.user.id == int(self.kwargs['pk']):
#                 return OrganizerUser.objects.only('id', 'email', 'username', 'second_name')
#             else:
#                 logger.error('User with ID %s cannot get user instance with ID %s' % (self.request.user.id, self.kwargs['pk']))
#                 raise exceptions.PermissionDenied('Cant get user with ID %s for user_retrieve_view' % self.kwargs['pk'])
#         except ObjectDoesNotExist:
#             logger.error('User with ID %s does not exist' % self.request.user.id)
#             raise exceptions.NotFound('Cant get user with ID %s for user_retrieve_view' % self.request.user.id)



def jwt_response_handler_user(token, user=None, *args):        # api-token-auth/
    token_data = {                                             # api-token-verify/
        'jwt_token': token,                                    # api-token-refresh/
        'jwt_date': datetime.now(),
        'user_id': user.pk
    }
    try:
        organizer_user_item = OrganizerUser.objects.get(pk=token_data['user_id'])
        organizer_user_serializer = OrganizerUserSerializer(organizer_user_item, data={
            'jwt_token': token_data['jwt_token'], 'jwt_date': token_data['jwt_date']
        }, partial=True)
        organizer_user_serializer.is_valid(raise_exception=True)  # Return a 400 response if the data was invalid.
        organizer_user_serializer.save()
        logger.info(msg='Token for user with email %s was save' % organizer_user_serializer['email'])
        return {'token': token_data['jwt_token']}
    except AuthenticationFailed:
        logger.info(msg='Authentication Failed. Token for user with email %s was NOT made'
                        % organizer_user_serializer['email'])
        return Response ({'detail': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
