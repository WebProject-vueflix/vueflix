from django.db import models
from django.forms import CharField, DateTimeField
from django.conf import settings
# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)

class Videos(models.Model):
    key = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movies')
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    backdrop_path = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movie_review')
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)