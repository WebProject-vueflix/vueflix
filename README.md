# 최종관통프로젝트

### 1. 팀원 정보 및 업무 분담 내역

| 고승효                      | 김애리            |
| --------------------------- | ----------------- |
| 팀장<br />social login 구현 | dumpdata 받아오기 |

### 2. 목표 서비스 구현 및 실제 구현 정도



### 3. 데이터베이스 모델링 (ERD)

![ERD.drawio](image/ERD.drawio.png)

### 4. 필수 기능에 대한 설명



### 5. 배포 서버 URL



### 6. 일자별 기록

#### Day 1 - 220517

- social login 구현 - 내일 수업 들은 다음에 검증해보기
- dumpdata 받아오기 - json 파일로 받아오긴 했는데 1)리스트가 제대로 닫혀 있지 않는 문제, 2)원하는 데이터값을 받아오지 못하는 문제, 3)인코딩 에러 발생
  => context 들여쓰기 위치 문제로 정상적인 리스트로 받아옴.
  => 장르를 역참조해서 받아오는 방법을 생각해야할 것 같음 - 내일 다시 연구해보기
  => 인코딩 에러 해결 코드를 입력해줘도 해결되지 않음 - 내일 다시 연구해보기

#### Day 2 - 220518

- dumpdata 받아오기 - 계속 FK Error와 genre.set을 권고하는 메시지가 뜸.

  - 딕셔너리로 받아올 때,

  ```
  django.db.utils.IntegrityError: FOREIGN KEY constraint failed
  ```

  - create 할 때,

  ```
  direct assignment to the forward side of a many-to-many set is prohibited. use genres.set() instead.
  ```

  => 장르를 역참조해야 하는데 장르가 없어서 역참조해줄 대상이 없었다. 장르 데이터와 동시에 받아주어 에러 해결
  => 인코딩 에러 해결 코드를 입력해줘도 해결되지 않음 : ansure_ascii=False 옵션으로 해결

- dumpdata 받으면서 ERD를 수정해야함을 알고 ERD 새로 수정해주었다.

- dumpdata : {

  ​	MovieData => (NowPlayingMovie, PopularMovie, UpcomingMovie), 
  ​	NtoM => Genres, 
  ​	Serializers에서 처리해줄 데이터 => (Actors, Directors)
  }

- social login 확인

### 7. 느낀 점

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

```
python manage.py dumpdata --indent 4 movies.movie > test.json
```

