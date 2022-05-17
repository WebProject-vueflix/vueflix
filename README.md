# 최종관통프로젝트

### 1. 팀원 정보 및 업무 분담 내역

| 고승효 | 김애리 |
| ------ | ------ |
| 팀장   |        |

### 2. 목표 서비스 구현 및 실제 구현 정도



### 3. 데이터베이스 모델링 (ERD)

![ERD.drawio](image/ERD.drawio.png)

### 4. 필수 기능에 대한 설명



### 5. 배포 서버 URL



### 6. 느낀 점

- 고승효 : 
- 김애리 : 



DATA 받아오기

```python
from django.shortcuts import render
import requests
from .models import Movie
# Create your views here.

def index(request):

    data = Movie()

    for page in range(21,51):
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
                )


    context = {

        "movies": movies 
    }
    return render(request, 'movies/index.html', context)
```

