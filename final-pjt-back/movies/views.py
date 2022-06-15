from django.http import HttpResponse
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Director, Genre, PopularMovie,  Actor, Review
from .serializers.popularmovie import MovieListSerializer, MovieDetailSerializer
from .serializers.actor import ActorListSerializer, ActorDetailSerializer
from .serializers.director import DirectorDetailSerializer
from .serializers.review import ReviewSerializer
from .serializers.genre import GenreListSerializer, GenreDetailSerializer
from django.db.models import Count

API_KEY = '1084b2e96727cbe4bd9c2a0e2fd99168'
GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'

genre_dict_org = {
    '모험': 0,
    '판타지': 0,
    '애니메이션': 0,
    '드라마': 0,
    '공포': 0,
    '액션': 0,
    '코미디':0,
    '역사':0,
    '서부':0,
    '스릴러': 0,
    '범죄': 0,
    '다큐멘터리': 0,
    'SF': 0,
    '미스터리': 0,
    '음악': 0,
    '로맨스': 0,
    '가족': 0,
    '전쟁': 0,
    'TV 영화': 0
}

genre_dict = {
    '모험': 0,
    '판타지': 0,
    '애니메이션': 0,
    '드라마': 0,
    '공포': 0,
    '액션': 0,
    '코미디':0,
    '역사':0,
    '서부':0,
    '스릴러': 0,
    '범죄': 0,
    '다큐멘터리': 0,
    'SF': 0,
    '미스터리': 0,
    '음악': 0,
    '로맨스': 0,
    '가족': 0,
    '전쟁': 0,
    'TV 영화': 0
}

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

username = ''
@api_view(['GET',])
def movie_list(request):
    global username
    global genre_dict
    global genre_dict_org
    movie_list = get_list_or_404(PopularMovie)
    #초기작업
    # if username == request.user.username:
    #     print('hello user')
    if username != request.user.username:
        genre_dict = genre_dict_org
        print(genre_dict)
        user = request.user
        username = user.username
        for movie1 in movie_list:
            movie1.genre_score = 0
            movie1.save()
        for genre1 in user.hate_genres.all():
        # print(genre)
            genre_dict[genre1.name] = -5
            # print(genre.popular_movies.all())
            for movie2 in genre1.popular_movies.all():
                movie2.genre_score -=5
                movie2.save()
        for in_movie in user.like_popular_movies.all():
            for genre2 in in_movie.genres.all():
                genre_dict[genre2.name] += 1
                for genre_movie in genre2.popular_movies.all():
                    genre_movie.genre_score += 1
                    genre_movie.save()
            print(in_movie)
    print(genre_dict)

    movies = PopularMovie.objects.annotate(
            like_count=Count('like_users', distinct=True),
            review_count=Count('review', distinct=True)
        ).order_by('-popularity')[:20]
    print(genre_dict)


    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET',])
def movie_detail(request,popularmovie_pk):
    movie = get_object_or_404(PopularMovie, pk=popularmovie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET',])
def recommendation(request):
    # global username
    # global genre_dict
    # if username == request.user.username:
    #     print('hello user')
    # else:
    #     user = request.user
    #     username = user.username
    #     print('not hello user')
    #     print(user)
    #     genre_dict = genre_dict_org
    #     # print(user.hate_genres.all())
    #     for i in user.hate_genres.all():
    #         print(genre_dict[i.name])
    #         print(i)
    #         genre_dict[i.name] = -5
    #     for j in user.like_popular_movies.all():
    #         print(j)
    #         print(j.genres.all())
    #         # for k in j.genres.all():
    #         #     print(k)
    #         #     # for l in k.popular_movies.all():
    #         #     #     print(l)
    #         #     # 해당 장르의 영화들 (나중에 -해줄 것)
    #         #     print(k.popular_movies.all())
    #     print(genre_dict)
    # print(genre_dict)
    # user = request.user
    # username = request.user.username
    # print(username)
    # print(user)
    # print(type(user.username))
    # print(type(username))
    # print(type(user))
    # print(user.username)
    # if user.username == username:
    #     print('hello')
    # else:
    #     print('not hello')

    movie_list = PopularMovie.objects.annotate(
        like_count=Count('like_users', distinct=True),
        review_count=Count('review', distinct=True),
    ).order_by('-genre_score')[:20]
    print(genre_dict)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def genre_list(request):
    genres = get_list_or_404(Genre)

    # for genre in genres:
    #     print(genre.score)
    #     print(genre.unlike)
    #     genre.score = 0
    #     genre.unlike = False
    #     genre.save()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def genre_detail(request,genre_pk):
    genre = get_object_or_404(Genre,pk=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)

@api_view(['POST'])
def unlike_genre(request, genre_pk):
    global genre_dict
    # global username
    genre = get_object_or_404(Genre, pk=genre_pk)
    # if username != request.user.username:
    #     user = request.user
    #     username = user.username
    #     genre_dict = genre_dict_org
    #     for genre in user.hate_genres.all():
    #         # print(genre)
    #         genre_dict[genre.name] = -5
    #         print(genre.popular_movies.all())
    #         # for movie in genre.popular_movies.all():
    #         #     movie.genre_score -=5
    #         #     movie.save()
    #     print(genre_dict)
    # else: #username == request.user.username:
    #     print('same user')
        # print(genre_dict)
    user = request.user
    if genre.hate_users.filter(pk=user.pk).exists():
        genre.hate_users.remove(user)
        genre_dict[genre.name] = 0
        print(genre.popular_movies.all())
        for movie in genre.popular_movies.all():
            movie.genre_score += 5
            movie.save()
        # serializer = GenreDetailSerializer(genre)
        # return Response(serializer.data)
    else:
        genre.hate_users.add(user)
        # print(genre.name)
        # print(type(genre.name))
        genre_dict[genre.name] = -5
        for movie in genre.popular_movies.all():
            movie.genre_score -= 5
            movie.save()
        # print(user.hate_genres.all())
        # print(genre_dict)
    print(genre_dict)
    serializer = GenreDetailSerializer(genre)
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
    global genre_dict
    # global username
    # if username != request.user.username:
    #     user = request.user
    #     username = user.username
    #     genre_dict = genre_dict_org
    #     for in_movie in user.like_popular_movies.all():
    #         for genre in in_movie.genres.all():
    #             genre_dict[genre] += 1
    #             for genre_movie in genre.popular_movies.all():
    #                 genre_movie.genre_score += 1
    #                 genre_movie.save()
    #         print(in_movie)
    #         # genre_dict[in_movie.genre_score] += 1
    #     print(genre_dict)
    # else:
    #     print('hello')

    movie = get_object_or_404(PopularMovie, pk=popularmovie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        # print(movie.genres.all())
        # print('remove')
        # print(user.like_popular_movies.all())
        # for genre in movie.genres.all():
        #     if genre.score > 0:
        #         genre.score = genre.score - 1
        #         genre.save()
        for genre1 in movie.genres.all():
            if genre_dict[genre1.name] > 0:
                genre_dict[genre1.name] -= 1
                for movie1 in genre1.popular_movies.all():
                    movie1.genre_score -= 1
                    movie1.save()
        # print(genre_dict)
        movie.like_users.remove(user)

    else:
        movie.like_users.add(user)
        # print(movie.genres.all())
        for genre2 in movie.genres.all():
            # print(genre)
            # print(type(genre.name))
            if genre_dict[genre2.name] >= 0:
                genre_dict[genre2.name] += 1
                for movie2 in genre2.popular_movies.all():
                    movie2.genre_score += 1
                    movie2.save()
        #     print(genre_dict[genre.name])
        # print('add')
        # print(genre_dict)
        # for genre in movie.genres.all():
        #     if genre.score >= 0:
        #         genre.score = genre.score + 1
        #         genre.save()
    # b = 0
    # for genre in movie.genres.all():
    #     b += 0
    # movie.genre_score = b
    # movie.save()
    # for genre in movie.genres.all():
    #     print(genre)

    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def like_actor(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    user = request.user
    if actor.like_users.filter(pk=user.pk).exists():
        actor.like_users.remove(user)
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)
    else:
        actor.like_users.add(user)
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)

@api_view(['POST'])
def like_director(request, director_pk):
    director = get_object_or_404(Director, pk=director_pk)
    user = request.user
    if director.like_users.filter(pk=user.pk).exists():
        director.like_users.remove(user)
        serializer = DirectorDetailSerializer(director)
        return Response(serializer.data)
    else:
        director.like_users.add(user)
        serializer = DirectorDetailSerializer(director)
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