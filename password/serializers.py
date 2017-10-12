from rest_framework import serializers

from accounts.models import OrganizerUser
from .models import PasswordOrganizer


class PasswordOrganizerListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = PasswordOrganizer
        fields = ('__all__')


class PasswordOrganizerSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = PasswordOrganizer
        fields = ('__all__')

    def create(self, validated_data):
        user = OrganizerUser.objects.get(pk=self.owner)
        return PasswordOrganizer.objects.create(owner=user.id, resource_url=validated_data.pop('resource_url'),
                                                password_res=validated_data.pop('password_res'))