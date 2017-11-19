from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import OrganizerUser


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


class LoginSerializer(serializers.Serializer):
    user_mail = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=30, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        user_mail = data.get('user_mail', None)
        password = data.get('password', None)
        if user_mail is None:
            raise serializers.ValidationError('An user_mail address is required to log in.')
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')
        user = authenticate(user_mail=user_mail, password=password)
        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')
        return {
            'user_mail': user.user_mail,
            'token': user.token
        }

class OrganizerUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = OrganizerUser
        fields = '__all__'


class OrganizerUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = '__all__'
