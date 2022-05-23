from django.urls import path
from . import views

# app_name='movies'
urlpatterns = [
    # 전체 movie 조회
    path('', views.movie_list),
    # 무비 detail
    path('<int:popularmovie_pk>/',views.movie_detail),
    # 무비 좋아요
    path ('<int:popularmovie_pk>/like/', views.like_movie),
    # 배우 list
    path('actor/', views.actor_list),
    # 배우 detail
    path('actor/<int:actor_pk>/', views.actor_detail),
    # 배우 좋아요
    path('actor/<int:actor_pk>/like/', views.like_actor),
    # 감독 detail
    path('director/<int:director_pk>/', views.director_detail),
    # 감독 좋아요
    path('director/<int:director_pk>/like/', views.like_director),
    # movie 내부 review create
    path('<int:popularmovie_pk>/reviews/', views.review_create),
    # movie 내부 review list/delete/update
    # path('<int:popularmovie_pk>/reviews/<int:review_pk>/', views.review_list_or_delete_update),
    path('<int:popularmovie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),

]