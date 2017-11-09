from rest_framework import serializers

from .models import OrganizerUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = OrganizerUser
        fields = ['user_mail', 'first_name', 'password', 'token']

    def create(self, validated_data):
        return OrganizerUser.objects.create_user(**validated_data)


class OrganizerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = '__all__'


class OrganizerUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = '__all__'
