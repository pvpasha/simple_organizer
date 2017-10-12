from rest_framework import serializers

from accounts.models import OrganizerUser
from .models import Diary


class DiaryListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)
    #owner = serializers.PrimaryKeyRelatedField(read_only=True)
    #owner = serializers.CharField(read_only=True, source='owner.username')

    class Meta:
        model = Diary
        fields = ('owner','title', 'body', 'creation_date')

class DiarySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    class Meta:
        model = Diary
        fields = ('owner','title', 'body', 'creation_date')

    def create(self, validated_data):
        user = OrganizerUser.objects.get(pk=self.owner)
        return Diary.objects.create(owner=user.id,
                                    title=validated_data.pop('title'),
                                    body=validated_data.pop('body'))
        # owner_data = validated_data.pop('owner')
        # title_data = validated_data.pop('title')
        # body_data = validated_data.pop('body')
        # user = OrganizerUser.objects.get(user_mail=owner_data)
        # return Diary.objects.create(owner=user, title=title_data, body=body_data)