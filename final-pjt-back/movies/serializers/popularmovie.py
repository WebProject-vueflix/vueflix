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
    

    like_count = serializers.IntegerField()
    review_count = serializers.IntegerField()

    class Meta:
        model = PopularMovie
        fields = ('id', 'title', 'adult', 'release_date', 'vote_average', 'poster_path', 'genres', 'actors', 'director','like_count', 'review_count', 'genre_score')
        read_only_fields = ('genres', 'actors', 'director',)

class MovieDetailSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)
    # genres = GenreSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True)

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
    # class ActorSerializer(serializers.ModelSerializer):

    #     class Meta:
    #         model = Actor
    #         fields = ('id', 'name', 'profile_path','character',)
    # # actors = ActorSerializer(many=True, read_only=True)
    # actors = ActorSerializer(many=True)
    actors = ActorDetailSerializer(many=True)

    class DirectorSerializer(serializers.ModelSerializer):
        class DirectorMovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = PopularMovie
                fields = ('id', 'title', 'poster_path')
        popular_movies = DirectorMovieSerializer(many=True)
        class Meta:
            model = Director
            fields = ('id', 'name', 'profile_path', 'popular_movies')
    # director = DirectorSerializer(many=True, read_only=True)
    director = DirectorSerializer(many=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk','title','content','user','like_users','rank','created_at','updated_at',)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = PopularMovie
        fields = '__all__'

# class MovieReviewSerializer(serializers.ModelSerializer):
    
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('pk', 'username')
    
#     class ReviewListSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Review
#             fields = ('title','content','rank')
#     movie_review = ReviewSerializer(many=True, read_only=True)
#     user = UserSerializer(read_only=True)
#     # like_count = serializers.IntegerField()

#     class Meta:
#         model = PopularMovie
#         fields = ('pk', 'user', 'movie_review',)
