from rest_framework import serializers

from accounts.models import OrganizerUser
from .models import Contact


class ContactListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Contact
        fields = ('__all__')


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Contact
        fields = ('__all__')

    # def create(self, validated_data):
    #     user = OrganizerUser.objects.get(pk=self.owner)
    #     return Contact.objects.create(owner=user.id,
    #                                   name=validated_data.pop('name'),
    #                                   surname=validated_data.pop('surname'),
    #                                   phone=validated_data.pop('phone'),
    #                                   birthday=validated_data.pop('birthday'),
    #                                   )
        # owner_data = validated_data.pop('owner')
        # title_data = validated_data.pop('title')
        # body_data = validated_data.pop('body')
        # user = OrganizerUser.objects.get(user_mail=owner_data)
        # return Contact.objects.create(owner=user, title=title_data, body=body_data)