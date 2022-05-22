from dataclasses import field
from rest_framework import serializers
from ..models import Actor, PopularMovie
from accounts.models import User

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'character',)

class ActorDetailSerializer(serializers.ModelSerializer):

    class ActorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = PopularMovie
            fields = ('id', 'title', 'poster_path')
    popular_movies = ActorMovieSerializer(many=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'profile_path', 'character', 'popular_movies')
        read_only_fields = ('popular_movies',)


