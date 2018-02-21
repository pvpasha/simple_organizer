import logging

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status, exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin

from .models import OrganizerUser
from .serializers import UserSerializer, UserListSerializer, UserProfileSerializer


logger = logging.getLogger(__name__)


class RegistrationAPIView(CreateAPIView):       # >> sing-up/
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
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
            logger.error('Can not create user with email: "%s" and name: "%s". Passwords does not match at '
                         'RegistrationAPIView' % (user_data['email'], user_data['username']))
            return ValidationError('Can not create. Passwords does not match', code=status.HTTP_417_EXPECTATION_FAILED)


class UserListView(ListAPIView):        # >> user-list/
    permission_classes = (AllowAny,)
    serializer_class = UserListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            user_inst = OrganizerUser.objects.get(pk=self.request.user.id)
        except ObjectDoesNotExist:
            logger.error('User with ID %s does not exist' % self.request.user.id)
            raise exceptions.NotFound('Cant get user with ID %s for UserListView' % self.request.user.id)
        if user_inst.is_staff:
            return OrganizerUser.objects.order_by('id')
        else:
            logger.error('User with ID %s have no permissions to users instances' % self.request.user.id)
            raise exceptions.PermissionDenied('User with ID %s have no permissions to users instances'
                                              % self.request.user.id)


class UserRetrieveView(RetrieveAPIView):        # >> profile/email/
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer
    lookup_field = 'email'

    def get_queryset(self):
        try:
            if self.request.user.email == self.kwargs['email']:
                return OrganizerUser.objects.all()
            else:
                logger.error('User with email %s cannot get user instance with email %s' % (
                    self.request.user.email, self.kwargs['email']))
                raise exceptions.PermissionDenied('Cant get user with email %s for user_retrieve_view'
                                                  % self.kwargs['email'])
        except ObjectDoesNotExist:
            logger.error('User with email %s does not exist' % self.request.user.email)
            raise exceptions.NotFound('Cant get user with email %s for user_retrieve_view' % self.request.user.email)


class UserNameUpdateView(UpdateAPIView):        # >> profile-name/email/
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer
    lookup_field = 'email'

    def get_queryset(self):
        try:
            if self.request.user.email == self.kwargs['email']:
                return OrganizerUser.objects.all()
            else:
                logger.error('User with email %s cannot get user instance with email %s' % (
                    self.request.user.email, self.kwargs['email']))
                raise exceptions.PermissionDenied('Can not get user with email %s for UserNameUpdateView'
                                                  % self.kwargs['email'])
        except ObjectDoesNotExist:
            logger.error('User with email %s does not exist' % self.request.user.email)
            raise exceptions.NotFound('Can not get user with email %s for UserNameUpdateView' % self.request.user.email)

    def filter_queryset(self, queryset):
        pass


class UserAvatarUpdateView(UpdateAPIView):        # >> profile-avatar/email/
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'email'

    def get_queryset(self):
        try:
            if self.request.user.email == self.kwargs['email']:
                return OrganizerUser.objects.all()
            else:
                logger.error('User with email %s cannot get user instance with email %s' % (
                    self.request.user.email, self.kwargs['email']))
                raise exceptions.PermissionDenied('Can not get user with email %s for UserAvatarUpdateView'
                                                  % self.kwargs['email'])
        except ObjectDoesNotExist:
            logger.error('User with email %s does not exist' % self.request.user.email)
            raise exceptions.NotFound('Can not get user with email %s for UserAvatarUpdateView'
                                      % self.request.user.email)

    def update(self, request, *args, **kwargs):
        avatar = self.request.FILES['avatar']
        fs = FileSystemStorage()
        file_name = fs.save(avatar.name, avatar)
        file_url = fs.url(file_name)
        print(file_url)


class UserEmailUpdateView(UpdateAPIView):        # >> profile-email/pk/
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            if self.request.user.id == self.kwargs['pk']:
                return OrganizerUser.objects.all()
            else:
                logger.error('User with id %s cannot get user instance with id %s' % (
                    self.request.user.id, self.kwargs['pk']))
                raise exceptions.PermissionDenied('Can not get user with id %s for UserEmailUpdateView'
                                                  % self.kwargs['pk'])
        except ObjectDoesNotExist:
            logger.error('User with id %s does not exist' % self.request.user.id)
            raise exceptions.NotFound('Can not get user with id %s for UserEmailUpdateView' % self.request.user.id)


class UserEmailVerifyView(UpdateAPIView):        # >> email-verify/
    pass


class UserPasswordUpdateView(UpdateAPIView):        # >> password-update/email/
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'email'

    def get_queryset(self):
            try:
                if self.request.user.email == self.kwargs['email']:
                    return OrganizerUser.objects.all()
                else:
                    logger.error('msg')
            except ObjectDoesNotExist:
                logger.error('msg')
                raise exceptions.NotFound('msg')

    def update(self, request, *args, **kwargs):
        try:
            if request.data['password_new1'] == request.data['password_new2'] != request.data['password_old']:
                inst_user = OrganizerUser.objects.get(email=self.request.user.email)
                serializer_user = UserProfileSerializer(inst_user)
                password_user = serializer_user.data['password']
                password_old = request.data['password_old']
                password_new = request.data['password_new1']
                if check_password(password_old, encoded=password_user):
                    inst_user.password = make_password(password_new, salt=None, hasher='pbkdf2_sha256')
                    inst_user.save()
                    logger.info('Update password for user %s' % self.request.user.email)
                    return Response(serializer_user.data, status=status.HTTP_200_OK)
                else:
                    raise exceptions.AuthenticationFailed(
                        'Error update for user %s, check_password at UserPasswordUpdateView' % self.request.user.email)
            else:
                logger.error('Error update for user %s, password1!=password2 (or password_new1==password_old)'
                             ' at UserPasswordUpdateView' % self.request.user.email)
                raise exceptions.AuthenticationFailed(
                    'Error update for user %s, password1!=password2 (or password_new1==password_old)'
                    ' at UserPasswordUpdateView' % self.request.user.email)
        except ObjectDoesNotExist:
            logger.error('Error update for user %s at UserPasswordUpdateView' % self.request.user.email)
            raise exceptions.NotFound('Error update for user %s at UserPasswordUpdateView' % self.request.user.email)


class UserPasswordResetView(UpdateAPIView):        # >> password-reset/
    pass


def jwt_response_handler_user(token, user=None, *args):        # >> api-token-auth/
    token_data = {                                             # >> api-token-verify/
        'jwt_token': token,                                    # >> api-token-refresh/
        'jwt_date': datetime.now(),
        'user_id': user.pk
    }
    try:
        user_item = OrganizerUser.objects.get(pk=token_data['user_id'])
        user_serializer = UserSerializer(user_item, data={
            'jwt_token': token_data['jwt_token'], 'jwt_date': token_data['jwt_date']
        }, partial=True)
        user_serializer.is_valid(raise_exception=True)  # Return a 400 response if the data was invalid.
        user_serializer.save()
        logger.info(msg='Token for user with email %s was save' % user_serializer['email'])
        return {'token': token_data['jwt_token']}
    except AuthenticationFailed:
        logger.error(msg='Authentication Failed. Token for user with email %s was NOT made'
                         % user_serializer['email'])
        return Response({'detail': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
