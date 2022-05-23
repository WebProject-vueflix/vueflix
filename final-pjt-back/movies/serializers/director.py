from rest_framework import serializers
from ..models import Director, PopularMovie
from accounts.models import User

# class DirectorDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Director
#         fields = ('id', 'name', 'profile_path',)

class DirectorDetailSerializer(serializers.ModelSerializer):

    class DirectorMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = PopularMovie
            fields = ('id', 'title', 'poster_path')
    popular_movies = DirectorMovieSerializer(many=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)


    class Meta:
        model = Director
        fields = ('id', 'name', 'profile_path', 'popular_movies','user','like_users')
        read_only_fields = ('popular_movies',)