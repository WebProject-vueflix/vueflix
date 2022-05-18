from dataclasses import field
import requests
import json

# def get_movie():
#     def get_genre():
#         base_url = 'https://api.themoviedb.org/3'
#         path = '/genre/movie/list'

#         params = {
#             'api_key' : '1084b2e96727cbe4bd9c2a0e2fd99168',
#             'language' : 'ko',
#         }
#         res_genre = requests.get(base_url + path, params=params)
#         genre_list = res_genre.json()
        
        

# actor_ids = []
# movie_ids = []
# def get_movie_datas():

#     movies = []
#     for page in range(1,3):
#         url = "https://api.themoviedb.org/3/movie/popular?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR&page="
#         pageurl= url + str(page)
#         movielist = requests.get(pageurl).json()

#         for movie in movielist['results']:
#             if movie.get('release_date', ''):
#                 fields = {
#                     'adult':movie['adult'],
#                     'movie_id': movie['id'],
#                     'actor': movie['id'],
#                     'title': movie['title'],
#                     'release_date': movie['release_date'],
#                     'popularity': movie['popularity'],
#                     'vote_average': movie['vote_average'],
#                     'overview': movie['overview'],
#                     'backdrop_path': movie['backdrop_path'],
#                     'poster_path': movie['poster_path'],
#                     'genres': movie['genre_ids']
#                 }

#                 data = {
#                     'id':movie['id'],
#                     "model": "movies.popular",
#                     "fields": fields
#                 }

#                 movies.append(data)
#                 movie_ids.append(movie['id'])
#     with open("populardata.json", "w", encoding="utf-8") as w:
#         json.dump(movies, w, indent=4, ensure_ascii=False)

# get_movie_datas() 
# print(movie_ids)
# def get_actor():
#     actors=[]
#     for movie_id in movie_ids:
#         # print(movie_id)
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR"
#         actorlist = requests.get(url).json()
#         for actor in actorlist['cast']:
#             if actor['known_for_department'] == 'Acting' and actor['order']<=10:
#                 fields = {
#                     'movie_id': actorlist['id'],
#                     'name':actor['name'],
#                     'profile_path':actor['profile_path'],
#                     'character':actor['character'],
#                 }
#                 data = {
#                     'pk': actor['id'],
#                     "model": "movies.actor",
#                     "fields": fields
#                 }
#                 actors.append(data)
    
#     with open("actor2.json", "w", encoding="utf-8") as w:
#         json.dump(actors, w, indent=4, ensure_ascii=False)

# get_actor()


# dirctor_list= []
movie_ids=[]
movie_list = []
def get_movie_datas():
    movies = []
    for page in range(1,2):
        url = "https://api.themoviedb.org/3/movie/popular?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR&page="
        pageurl= url + str(page)
        movielist = requests.get(pageurl).json()

        for movie in movielist['results']:
            if movie.get('release_date', ''):
                fields = {
                    'genres': movie['genre_ids'],
                    'director': [],
                    'actor': [],
                    'adult':movie['adult'],
                    'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'backdrop_path': movie['backdrop_path'],
                    'poster_path': movie['poster_path']
                }
                
                data = {
                    "pk": movie['id'],
                    "model": "movies.popularmovie",
                    "fields": fields
                }

                movies.append(data)
                movie_ids.append(movie['id'])
    # 감독/배우 정보가 있는 경우, 추가로 받아온다.
    for data in movies:
        movie_id = data['fields']['movie_id']
        
        credit_request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR"
        credit_info = requests.get(credit_request_url).json()

        # 배우는 최대 10명까지만 저장한다.
        for cast in credit_info['cast'][:10]:
            data['fields']['actor'].append(cast['id'])
            # actor_list.append(cast['id'])
        for crew in credit_info['crew']:
            if crew['job']=="Director":
                data['fields']['director'].append(crew['id'])
                # dirctor_list.append(crew['id'])
    
    print(data['fields']['actor'])
    print(data['fields']['director'])
    with open("movie_data4.json", "w", encoding="utf-8") as w:
        json.dump(movies, w, indent="\t", ensure_ascii=False)



get_movie_datas()
print(movie_ids)

actors=[]
def get_actor():
           # data = Movie()
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR"
        actorlist = requests.get(url).json()
        for actor in actorlist['cast']:
            if actor['known_for_department'] == 'Acting' and actor['order']<10:
                fields = {
                    'name':actor['name'],
                    'profile_path':actor['profile_path'],
                    'character':actor['character'],
                }
                data = {
                    'pk': actor['id'],
                    "model": "movies.actor",
                    "fields": fields
                }
                actors.append(data)
    print(actors)
    with open("actor.json", "w", encoding="utf-8") as w:
        json.dump(actors, w, indent=4, ensure_ascii=False)

get_actor()

directors=[]
def get_directors():
           # data = Movie()
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko-KR"
        directorlist = requests.get(url).json()
        for director in directorlist['crew']:
            if director['job'] == 'Director':
                fields = {
                    'name':director['name'],
                    'profile_path':director['profile_path'],
                }
                data = {
                    'pk': director['id'],
                    "model": "movies.director",
                    "fields": fields
                }
                directors.append(data)
    print(directors)
    with open("directors.json", "w", encoding="utf-8") as w:
        json.dump(directors, w, indent=4, ensure_ascii=False)

get_directors()

