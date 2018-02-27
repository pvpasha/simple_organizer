from rest_framework import serializers

from .models import PasswordOrganizer


class PasswordOrganizerSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PasswordOrganizer
        fields = '__all__'
