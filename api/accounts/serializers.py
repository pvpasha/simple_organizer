from rest_framework import serializers

from .models import OrganizerUser


class OrganizerUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = OrganizerUser
        fields = '__all__'


class OrganizerUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = ('id', 'email', 'username', 'second_name')
