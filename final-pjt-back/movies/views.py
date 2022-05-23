from django.http import HttpResponse
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Director, Genre, PopularMovie, NowPlayingMovie, UpcomingMovie, Actor, Review
from .serializers.popularmovie import MovieListSerializer, MovieDetailSerializer
from .serializers.actor import ActorListSerializer, ActorDetailSerializer
from .serializers.director import DirectorDetailSerializer
from .serializers.review import ReviewSerializer

from django.db.models import Count

API_KEY = '1084b2e96727cbe4bd9c2a0e2fd99168'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'

def genre_data():
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',            
        }
    ).json()

    for genre in response.get('genres'):
        Genre.objects.create(
            id=genre.get('id'),
            name=genre.get('name')
        )
    return HttpResponse(response)

def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

# movie에 출연한 배우 정보
def get_actors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    
    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        if not Actor.objects.filter(pk=actor_id).exists():
            Actor.objects.create(
                id=person.get('id'),
                name=person.get('name'),
                profile_path=person.get('profile_path'),
                character=person.get('character')
            )
        movie.actors.add(actor_id)
        if movie.actors.count() == 5:
            break

def get_directors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    
    for person in response.get('crew'):
        if person.get('job') != 'Director': continue
        director_id = person.get('id')
        if not Director.objects.filter(pk=director_id).exists():
            Director.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
        movie.director.add(director_id)
        if movie.director.count() == 1:
            break

def movie_data(page=1):
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',     
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)
        
        movie = PopularMovie.objects.create(
            id=movie_dict.get('id'),
            adult=movie_dict.get('adult'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            backdrop_path=movie_dict.get('backdrop_path'),   
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key         
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        get_actors(movie)
        # get_directors(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)

def tmdb(request):
    Genre.objects.all().delete
    Actor.objects.all().delete
    PopularMovie.objects.all().delete

    genre_data()
    # for i in range(1,51):
    #         movie_data(i)
    return HttpResponse('OK')

@api_view(['GET',])
def movie_list(request):
    # movies = get_list_or_404(PopularMovie)
    movies = PopularMovie.objects.annotate(
            like_count=Count('like_users', distinct=True)
        ).order_by('-popularity')[:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def movie_detail(request,popularmovie_pk):
    movie = get_object_or_404(PopularMovie, pk=popularmovie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET',])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def actor_detail(request,actor_pk):
    actor = get_object_or_404(Actor,pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET',])
def director_detail(request,director_pk):
    director = get_object_or_404(Director,pk=director_pk)
    serializer = DirectorDetailSerializer(director)
    return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, popularmovie_pk):
    movie = get_object_or_404(PopularMovie, pk=popularmovie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def review_create(request, popularmovie_pk):
    user = request.user
    
    popular_movie =  get_object_or_404(PopularMovie,pk=popularmovie_pk)
    
    seralizer = ReviewSerializer(data=request.data)
    if seralizer.is_valid(raise_exception=True):
        seralizer.save(popular_movie=popular_movie, user=user)

        reviews = popular_movie.review_set.all()
        seralizer = ReviewSerializer(reviews,many=True)
        return Response(seralizer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
def review_update_or_delete(request, popularmovie_pk, review_pk):
    movie = get_object_or_404(PopularMovie,pk=popularmovie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.review_set.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)
        
    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.review_set.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)

    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()