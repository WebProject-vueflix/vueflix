from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import PopularMovie,Review

# like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_popular_movies')
# like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
# user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_review')

class ProfileSerializer(serializers.ModelSerializer):

    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = PopularMovie
            fields = ('pk','poster_path','title',)

    like_popular_movies = MovieListSerializer(many=True)

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('popular_movie','title','content',)
        
    movie_review = ReviewSerializer(serializers.ModelSerializer)


    class Meta:
        model = get_user_model()
        fields = ('username','like_popular_movies',)