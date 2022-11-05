from rest_framework import serializers
from .models import News


class NewsCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id",)


