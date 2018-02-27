from rest_framework import serializers

from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Diary
        fields = '__all__'
