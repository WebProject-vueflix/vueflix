from django.shortcuts import render
import requests
from .models import Movie
# Create your views here.

def index(request):
    # url = "https://api.themoviedb.org/3/movie/popular?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko&page="
    # pageurl= url + str(page)


    # BASE_URL = 'https://api.themoviedb.org/3'
    # path = '/movie/popular'
    # params = {
    #     'api_key': '1084b2e96727cbe4bd9c2a0e2fd99168',
    #     'language': 'ko',
    #     'region': 'KR',
    # }
    # response = requests.get(BASE_URL + path, params=params)
    # data=response.json()
    # print(response.status_code, response.url)
    # movielist = data.get('results')
    # print(len(movielist))

    data = Movie()

    movies = []
    for page in range(1,51):
        url = "https://api.themoviedb.org/3/movie/top_rated?api_key=1084b2e96727cbe4bd9c2a0e2fd99168&language=ko&page="
        pageurl= url + str(page)

        response = requests.get(pageurl)
        data=response.json()
        print(response.status_code, response.url)
        movielist = data.get('results')
        # print(len(movielist))
        for i in range(20):
            if movielist[i].get('release_date'):
                data = Movie.objects.create(
                title = movielist[i].get('title'),
                release_date = movielist[i].get('release_date'),
                popularity = movielist[i].get('popularity'),
                vote_average = movielist[i].get('vote_average'),
                overview = movielist[i].get('overview'),
                backdrop_path = movielist[i].get('backdrop_path'),
                poster_path = movielist[i].get('poster_path'),
                id = movielist[i].get('id'),
                )
            print(data.release_date)
            # data.save()


    context = {

        "movies": movies 
    }
    return render(request, 'movies/index.html', context)