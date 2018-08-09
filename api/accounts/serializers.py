from rest_framework import serializers

from .models import OrganizerUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = OrganizerUser
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = ('id', 'email', 'username', 'second_name')


class UserProfileViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = ('email', 'username', 'second_name', 'avatar')


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30)

    class Meta:
        model = OrganizerUser
        fields = ('id', 'email', 'password', 'username', 'second_name', 'avatar')
