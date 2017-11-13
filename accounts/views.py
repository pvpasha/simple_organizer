from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_417_EXPECTATION_FAILED
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from social_django.models import UserSocialAuth

from .renderers import UserJSONRenderer
from .models import OrganizerUser
from .serializers import OrganizerUserListSerializer, OrganizerUserSerializer  # RegistrationSerializer
from todo.views import main


class RegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = OrganizerUserSerializer
    queryset = OrganizerUser.objects.all()

    def post(self, request, *args, **kwargs):
        user_data = request.data
        if user_data['password1'] == user_data['password2']:

            user = OrganizerUser.objects.create_user(user_mail=user_data['user_mail'],
                                                     first_name=user_data['first_name'],
                                                     password=user_data['password1'])
            serializer = self.get_serializer_class()
            return Response(serializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return ValidationError('Cannot create. Passwords does not match.', code=HTTP_417_EXPECTATION_FAILED)

        # 'user_mail', 'first_name', 'password'
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrganizerUserItemView(RetrieveAPIView):
    queryset = OrganizerUser.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = OrganizerUserSerializer
    lookup_field = 'user_mail'


class OrganizerUserViewSet(ListCreateAPIView):
    queryset = OrganizerUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = OrganizerUserListSerializer

    def post(self, request, *args, **kwargs):
        get_user_mail = request.data['user_mail']
        # get_password = request.data['password']
        get_first_name = request.data['first_name']
        get_second_name = request.data['second_name']
        try:
            organizer_user_item = OrganizerUser.objects.create_user(user_mail=get_user_mail,
                                                                    first_name=get_first_name,
                                                                    second_name=get_second_name)
            serialized_data = self.get_serializer(organizer_user_item)
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@login_required
def main(request):
    return render(request, main('main.html'))


@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/login.html', {'form': form})
