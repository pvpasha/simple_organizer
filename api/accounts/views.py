import logging

from datetime import datetime
from django.contrib.auth import logout, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_social_auth.serializers import UserSerializer
from rest_social_auth.views import JWTAuthMixin
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import OrganizerUser
from .serializers import OrganizerUserListSerializer, OrganizerUserSerializer


logger = logging.getLogger(__name__)


class RegistrationAPIView(CreateAPIView):
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
            logger.info('Can not create user with email: "%s" and name: "%s". Passwords does not match.' % (
                user_data['email'], user_data['username']))
            return ValidationError('Cannot create. Passwords does not match.', code=status.HTTP_417_EXPECTATION_FAILED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = (OrganizerUserSerializer,)

    def post(self, request):
        user_mail = request.data['email']
        user_pass = request.data['password']
        try:
            organizer_user_item = OrganizerUser.objects.get(email=user_mail['email'])
            organizer_user_serializer = OrganizerUserSerializer(organizer_user_item, data={
                'email': user_mail, 'password': user_pass['password']
            })
            # if user_pass ==OrganizerUser.objects.get(password)

            serializer = self.serializer_class(data=user_mail)
            serializer.is_valid(raise_exception=True)

            logger.info(msg='User with email: "%s" was login' % user_mail['email'])
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed:
            return Response({'detail': 'Authentication Failed'}, status=status.HTTP_401_UNAUTHORIZED)


class OrganizerUserItemView(RetrieveAPIView):
    queryset = OrganizerUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrganizerUserSerializer
    lookup_field = 'email'


class OrganizerUserViewSet(ListCreateAPIView):
    queryset = OrganizerUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = OrganizerUserListSerializer

    def post(self, request, *args, **kwargs):
        get_email = request.data['email']
        # get_password = request.data['password']
        get_first_name = request.data['first_name']
        get_second_name = request.data['second_name']
        try:
            organizer_user_item = OrganizerUser.objects.create_user(email=get_email,
                                                                    first_name=get_first_name,
                                                                    second_name=get_second_name)
            serialized_data = self.get_serializer(organizer_user_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutSessionView(APIView):

    def post(request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class BaseDetailView(generics.RetrieveAPIView):
    permission_classes = IsAuthenticated,
    serializer_class = UserSerializer
    model = get_user_model()

    def get_object(self, queryset=None):
        return self.request.user


class UserSessionDetailView(BaseDetailView):
    authentication_classes = (SessionAuthentication, )


class UserTokenDetailView(BaseDetailView):
    authentication_classes = (TokenAuthentication, )


class UserJWTDetailView(JWTAuthMixin, BaseDetailView):
    pass



def jwt_response_handler_user(token, user=None, *args):        # /api-token-auth/
    token_data = {                                             # /api-token-verify/
        'jwt_token': token,
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
