from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Director, Genre, PopularMovie, NowPlayingMovie, UpcomingMovie, Actor

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

# def get_youtube_key(movie_dict):    
#     movie_id = movie_dict.get('id')
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
#         params={
#             'api_key': API_KEY
#         }
#     ).json()
#     for video in response.get('results'):
#         if video.get('site') == 'YouTube':
#             return video.get('key')
#     return 'nothing'

# # movie에 출연한 배우 정보
# def get_actors(movie):
#     movie_id = movie.id
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()
    
#     for person in response.get('cast'):
#         if person.get('known_for_department') != 'Acting': continue
#         actor_id = person.get('id')
#         if not Actor.objects.filter(pk=actor_id).exists():
#             Actor.objects.create(
#                 id=person.get('id'),
#                 name=person.get('name'),
#                 profile_path=person.get('profile_path'),
#                 character=person.get('character')
#             )
#         movie.actors.add(actor_id)
#         if movie.actors.count() == 5:
#             break

# def get_directors(movie):
#     movie_id = movie.id
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',
#         }
#     ).json()
    
#     for person in response.get('crew'):
#         if person.get('job') != 'Director': continue
#         director_id = person.get('id')
#         if not Director.objects.filter(pk=director_id).exists():
#             Director.objects.create(
#                 id=person.get('id'),
#                 name=person.get('name')
#             )
#         movie.dirctor.add(director_id)
#         if movie.dirctor.count() == 1:
#             break

# def movie_data(page=1):
#     response = requests.get(
#         POPULAR_MOVIE_URL,
#         params={
#             'api_key': API_KEY,
#             'language': 'ko-kr',     
#             'page': page,       
#         }
#     ).json()

#     for movie_dict in response.get('results'):
#         if not movie_dict.get('release_date'): continue   # 없는 필드 skip
#         # 유투브 key 조회
#         youtube_key = get_youtube_key(movie_dict)
        
#         movie = PopularMovie.objects.create(
#             id=movie_dict.get('id'),
#             adult=movie_dict.get('adult'),
#             title=movie_dict.get('title'),
#             release_date=movie_dict.get('release_date'),
#             popularity=movie_dict.get('popularity'),
#             vote_average=movie_dict.get('vote_average'),
#             overview=movie_dict.get('overview'),
#             backdrop_path=movie_dict.get('backdrop_path'),   
#             poster_path=movie_dict.get('poster_path'),   
#             youtube_key=youtube_key         
#         )
#         for genre_id in movie_dict.get('genre_ids', []):
#             movie.genres.add(genre_id)

#         # 배우들 저장
#         get_actors(movie)
#         # get_directors(movie)
#         print('>>>', movie.title, '==>', movie.youtube_key)

# # from .models import Movie
# # Create your views here.

def index(request):
        # Genre.objects.all().delete
        # Actor.objects.all().delete
        # PopularMovie.objects.all().delete

        genre_data()
        # for i in range(1,51):
        #         movie_data(i)
        return HttpResponse('OK')
    # data = Movie()

    # movies = []
    # for page in range(1,51):
    #     url = "https://api.themoviedb.org/3/movie/top_rated?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR&page="
    #     pageurl= url + str(page)

    #     response = requests.get(pageurl)
    #     data=response.json()
    #     print(response.status_code, response.url)
    #     movielist = data.get('results')
    #     # print(len(movielist))
    #     for i in range(20):
    #         if movielist[i].get('release_date'):
    #             data = Movie.objects.create(
    #             title = movielist[i].get('title'),
    #             release_date = movielist[i].get('release_date'),
    #             popularity = movielist[i].get('popularity'),
    #             vote_average = movielist[i].get('vote_average'),
    #             overview = movielist[i].get('overview'),
    #             backdrop_path = movielist[i].get('backdrop_path'),
    #             poster_path = movielist[i].get('poster_path'),
    #             movie_id = movielist[i].get('id'),
    #             )
    #         # print(data.release_date)
    #         # data.save()


            # context = {

            #     "movies": movies 
            # }