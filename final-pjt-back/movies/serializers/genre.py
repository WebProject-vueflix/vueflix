from rest_framework import serializers
from ..models import Genre,PopularMovie
from accounts.models import User

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)

class GenreDetailSerializer(serializers.ModelSerializer):
    class GenreMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = PopularMovie
            fields = ('id', 'title', 'poster_path')
    popular_movies = GenreMovieSerializer(many=True)


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)
    user = UserSerializer(read_only=True)
    hate_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'hate_users','user','popular_movies')
        # read_only_fields = ('',)
