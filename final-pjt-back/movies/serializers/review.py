from rest_framework import serializers
from ..models import PopularMovie, Review
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user')


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = PopularMovie
            fields = ('title',)
    movies = MovieListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'rank', 'user', 'movies',)