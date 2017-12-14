
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import OrganizerUser
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers


from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username_field, PasswordField


# class TokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Token
#         fields = ('key',)


# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, min_length=8, write_only=True)
#     # token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#         model = OrganizerUser
#         fields = ['user_mail', 'first_name', 'password']
#
#     def create(self, validated_data):
#         return OrganizerUser.objects.create_user(**validated_data)


class OrganizerUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = OrganizerUser
        fields = '__all__'


class OrganizerUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = '__all__'
