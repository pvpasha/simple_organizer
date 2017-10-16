from rest_framework import serializers

from .models import OrganizerUser

class OrganizerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = '__all__'


class OrganizerUserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizerUser
        fields = '__all__'
