from dataclasses import fields
from rest_framework import serializers
from ..models import Genre, Actor, Director, PopularMovie, Review
from accounts.models import User
from .review import ReviewSerializer


class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)
    # genres = GenreSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True)

    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('name', 'character',)
    # actors = ActorSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True)

    class DirectorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Director
            fields = ('name',)
    # director = DirectorSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True)


    class Meta:
        model = PopularMovie
        fields = ('id', 'title', 'adult', 'release_date', 'vote_average', 'poster_path', 'genres', 'actors', 'director',)
        read_only_fields = ('genres', 'actors', 'director',)

class MovieDetailSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)
    # genres = GenreSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True)

    class ActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('id', 'name', 'profile_path','character',)
    # actors = ActorSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True)

    class DirectorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Director
            fields = ('id', 'name', 'profile_path',)
    # director = DirectorSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)
    review_set = ReviewSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = PopularMovie
        fields = '__all__'
