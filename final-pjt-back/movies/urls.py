from django.urls import path
from . import views

app_name='movies/'
urlpatterns = [
    path('', views.movie_list),
    path('<int:popularmovie_pk>/',views.movie_detail),
    path('actor/', views.actor_list),
    path('actor/<int:actor_pk>/', views.actor_detail),
    path('director/<int:director_pk>/', views.director_detail),
    path('actor/<int:popularmovie_id>/<int:user_pk>', views.review_list),
]