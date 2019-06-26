from rest_framework import serializers
from ..models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "image",
            "title",
            "slug",
            "publish"
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "image",
            'Mainimage',
            "title",
            "slug",
            "content",
            "publish",
        ]

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "image",
            'Mainimage',
            "title",
            "content",
            "publish",
        ]