from rest_framework import serializers

from accounts.models import OrganizerUser
from .models import Category, ShortTask, Task, Event


class CategoryListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Category
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Category
        fields = ('__all__')

    # def create(self, validated_data):
    #     user = OrganizerUser.objects.get(pk=self.owner)
    #     return PasswordOrganizer.objects.create(owner=user.id, resource_url=validated_data.pop('resource_url'),
    #                                             password_res=validated_data.pop('password_res'))


class ShortTaskListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = ShortTask
        fields = ('__all__')


class ShortTaskSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = ShortTask
        fields = ('__all__')


class TaskListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Task
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Task
        fields = ('__all__')


class EventListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Event
        fields = ('__all__')


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Event
        fields = ('__all__')