from django.db import models
from django.forms import CharField, DateTimeField
from django.conf import settings
# Create your models here.

class Actor(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actor')
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)
    character = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name


class Director(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_director')
    name = models.CharField(max_length=200)
    profile_path = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Genre(models.Model):
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_genres')
    score = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    unlike = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class PopularMovie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_popular_movies')
    genres = models.ManyToManyField(Genre, related_name='popular_movies')
    actors = models.ManyToManyField(Actor, related_name='popular_movies')
    director = models.ManyToManyField(Director, related_name='popular_movies')
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    youtube_key = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.title


class NowPlayingMovie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_nowplaying_movies')
    genres = models.ManyToManyField(Genre, related_name='nowplaying_movies')    
    actors = models.ManyToManyField(Actor, related_name='nowplaying_movies')
    director = models.ManyToManyField(Director, related_name='nowplaying_movies')
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    youtube_key = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.title

class UpcomingMovie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_upcoming_movies')
    genres = models.ManyToManyField(Genre, related_name='upcoming_movies')
    actors = models.ManyToManyField(Actor, related_name='upcoming_movies')
    director = models.ManyToManyField(Director, related_name='upcoming_movies')
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    youtube_key = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200, null=True)
    poster_path = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.title

class Review(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    popular_movie = models.ForeignKey(PopularMovie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_review')
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

