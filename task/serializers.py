from rest_framework import serializers

from .models import Category, ShortTask, Task, Event


class CategoryListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Category
        fields = '__all__'


class ShortTaskListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta():
        model = ShortTask
        fields = '__all__'


class ShortTaskSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True, many=False)

    class Meta():
        model = ShortTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Task
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    task_list = TaskSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Event
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    event_list = EventSerializer(read_only=True, many=True)

    class Meta:
        model = Event
        fields = '__all__'



