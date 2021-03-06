import logging

from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from rest_framework import status, exceptions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from .models import OrganizerUser
from .serializers import UserSerializer, UserListSerializer, UserProfileSerializer, UserProfileViewSerializer
from .tokens import account_activation_token


logger = logging.getLogger(__name__)


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = OrganizerUser.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data['password1'] == request.data['password2']:
            user = OrganizerUser.objects.create_user(email=request.data['email'],
                                                     username=request.data['username'],
                                                     password=request.data['password1'])
            serializer = self.get_serializer_class()
            current_site = get_current_site(request)
            mail_subject = 'Simple Organizer - Activate your account.'
            message = render_to_string('activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = request.data['email']
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            logger.info('User with email: "%s" and name: "%s" was created successful.'
                        % (request.data['email'], request.data['username']))
            return Response(serializer(user).data, status=status.HTTP_201_CREATED)
        else:
            logger.error('Can not create user with email: "%s" and name: "%s". Passwords does not match at '
                         'RegistrationAPIView' % (request.data['email'], request.data['username']))
            return exceptions.ValidationError('Can not create. Passwords does not match',
                                              code=status.HTTP_417_EXPECTATION_FAILED)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = OrganizerUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class UserListView(ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
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


class UserRetrieveView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileViewSerializer
    lookup_field = 'email'

    def get_queryset(self):
        try:
            if self.request.user.email == self.kwargs['email']:
                return OrganizerUser.objects.filter(email=self.request.user.email)
            else:
                logger.error('User with email %s cannot get user instance with email %s' % (
                    self.request.user.email, self.kwargs['email']))
                raise exceptions.PermissionDenied('Cant get user with email %s for user_retrieve_view'
                                                  % self.kwargs['email'])
        except ObjectDoesNotExist:
            logger.error('User with email %s does not exist' % self.request.user.email)
            raise exceptions.NotFound('Cant get user with email %s for user_retrieve_view' % self.request.user.email)


class UserNameUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileViewSerializer
    lookup_field = 'email'

    def get_queryset(self):
        try:
            if self.request.user.email == self.kwargs['email']:
                return OrganizerUser.objects.get(email=self.request.user.email)
            else:
                logger.error('User with email %s cannot get user instance with email %s' % (
                    self.request.user.email, self.kwargs['email']))
                raise exceptions.PermissionDenied('Can not get user with email %s for UserNameUpdateView'
                                                  % self.kwargs['email'])
        except ObjectDoesNotExist:
            logger.error('User with email %s does not exist' % self.request.user.email)
            raise exceptions.NotFound('Can not get user with email %s for UserNameUpdateView' % self.request.user.email)

    def update(self, request, *args, **kwargs):
        try:
            if request.data['username'] or request.data['second_name']:
                inst_user = OrganizerUser.objects.get(email=self.request.user.email)
                serializer_user = UserProfileViewSerializer(
                    inst_user, data={'username': request.data['username'], 'second_name': request.data['second_name']},
                    partial=True)
                serializer_user.is_valid()
                serializer_user.save()
                return Response(serializer_user.data, status=status.HTTP_200_OK)
            else:
                logger.error('Error update for user %s, bad request data at user_name_update_view'
                             % self.request.user.email)
                raise exceptions.ValidationError(
                    'Error update for user %s, bad request data' % self.request.user.email)
        except ObjectDoesNotExist:
            logger.error('Error update for user %s at user_name_update_view' % self.request.user.email)
            raise exceptions.NotFound('Error update for user %s' % self.request.user.email)


class UserAvatarUpdateView(UpdateAPIView):
    serializer_class = UserProfileViewSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'email'

    def get_queryset(self):
        try:
            if self.request.user.email == self.kwargs['email']:
                return OrganizerUser.objects.get(email=self.request.user.email)
            else:
                logger.error('User with email %s cannot get user instance with email %s for UserAvatarUpdateView'
                             % (self.request.user.email, self.kwargs['email']))
                raise exceptions.PermissionDenied('Can not get user with email %s' % self.kwargs['email'])
        except ObjectDoesNotExist:
            logger.error('User with email %s does not exist for UserAvatarUpdateView' % self.request.user.email)
            raise exceptions.NotFound('Can not get user with email %s ' % self.request.user.email)

    def update(self, request, *args, **kwargs):
        if self.request.FILES['avatar']:
            avatar = self.request.FILES['avatar']
            try:
                instance = self.get_queryset()
                if instance.avatar:
                    instance.avatar.delete()
                    instance.avatar.save(avatar.name, File(avatar))
                    instance.save()
                    serializer = self.get_serializer(instance)
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except TypeError:
                logger.error('Wrong file type')
                raise exceptions.ValidationError('Can not use this file type')
        else:
            logger.error('Avatar file was not sent')
            raise exceptions.NotFound('Can not find avatar file in files section of request')


class UserEmailUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileViewSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            if self.request.user.id == self.kwargs['pk']:
                return OrganizerUser.objects.get(email=self.request.user.email)
            else:
                logger.error('User with id %s cannot get user instance with id %s' % (
                    self.request.user.id, self.kwargs['pk']))
                raise exceptions.PermissionDenied('Can not get user with id %s for UserEmailUpdateView'
                                                  % self.kwargs['pk'])
        except ObjectDoesNotExist:
            logger.error('User with id %s does not exist' % self.request.user.id)
            raise exceptions.NotFound('Can not get user with id %s for UserEmailUpdateView' % self.request.user.id)

    def update(self, request, *args, **kwargs):
        pass


class UserEmailVerifyView(UpdateAPIView):
    pass


class UserPasswordUpdateView(UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'email'

    def get_queryset(self):
            try:
                if self.request.user.email == self.kwargs['email']:
                    return OrganizerUser.objects.get(email=self.request.user.email)
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


class UserPasswordResetView(UpdateAPIView):
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
    except exceptions.AuthenticationFailed:
        logger.error(msg='Authentication Failed. Token for user with email %s was NOT made'
                         % user_serializer['email'])
        return Response({'detail': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)
