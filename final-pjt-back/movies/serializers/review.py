from rest_framework import serializers
from ..models import PopularMovie, Review
from accounts.models import User



class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'user', 'popular_movie','created_at','updated_at')
        read_only_fields=('popular_movie',)