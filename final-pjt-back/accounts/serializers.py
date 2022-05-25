from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import PopularMovie,Review,Genre,Director,Actor

# like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_popular_movies')
# like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_review')

class ProfileSerializer(serializers.ModelSerializer):

    class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('score','name','id',)

    hate_genres = GenreListSerializer(many=True)


    class MovieListSerializer(serializers.ModelSerializer):
        
        class GenreListSerializer(serializers.ModelSerializer):
            class Meta:
                model = Genre
                fields = ('id','name',)
        genres = GenreListSerializer(many=True)

        class Meta:
            model = PopularMovie
            fields = ('pk','poster_path','title','genres')
    # genre = serializers.ManyRelatedFields
    like_popular_movies = MovieListSerializer(many=True)

    class ActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk','profile_path','name',)

    like_actor = ActorListSerializer(many=True)

    class DirectorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('pk','profile_path','name',)


    like_director = DirectorListSerializer(many=True)


    class ReviewSerializer(serializers.ModelSerializer):

        class MovieDetailSerializer(serializers.ModelSerializer):

            class Meta:
                model = PopularMovie
                fields = ('id', 'title', )

        popular_movie = MovieDetailSerializer()

        class Meta:
            model = Review
            fields = ('popular_movie','title','content','popular_movie',)
        
        
    movie_review = ReviewSerializer(many=True)


    class Meta:
        model = get_user_model()
        fields = ('username','like_popular_movies','movie_review','like_director','like_actor','hate_genres')