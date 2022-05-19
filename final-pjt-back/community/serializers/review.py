from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review
from .comment import CommentSerializer
# from .comment import CommentSerializer

User = get_user_model()

class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'comment_count', 'like_count')


class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    community_review = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'content', 'community_review', )