from django.db import models
from django.forms import CharField, DateTimeField
from django.conf import settings
# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)
    character = models.CharField(max_length=100)


class Director(models.Model):
    name = models.CharField(max_length=200)
    profile_path = models.CharField(max_length=200, null=True)

class Video(models.Model):
    key = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class PopularMovie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_popular_movies')
    genres = models.ManyToManyField(Genre, related_name='popular_movies')
    actor = models.ManyToManyField(Actor, related_name='popular_movies')
    director = models.ManyToManyField(Director, related_name='popular_movies')
    adult = models.BooleanField()
    movie_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)

class NowPlayingMovie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_nowplaying_movies')
    genres = models.ManyToManyField(Genre, related_name='nowplaying_movies')
    adult = models.BooleanField()
    movie_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)

class UpcomingMovie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_upcoming_movies')
    genres = models.ManyToManyField(Genre, related_name='upcoming_movies')
    adult = models.BooleanField()
    movie_id = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)

class Review(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    popular_movie = models.ForeignKey(PopularMovie, on_delete=models.CASCADE)
    nowplaying_movie = models.ForeignKey(NowPlayingMovie, on_delete=models.CASCADE)
    upcoming_movie = models.ForeignKey(UpcomingMovie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_review')
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

