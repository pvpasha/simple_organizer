from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
