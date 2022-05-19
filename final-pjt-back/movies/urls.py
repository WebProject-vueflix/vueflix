from django.urls import path
from . import views

app_name='movies/'
urlpatterns = [
    path('', views.movie_list),
    path('actor/', views.actor_list),
    path('actor/<int:actor_pk>/', views.actor_detail),
    path('actor/<int:popularmovie_id>/<int:user_pk>', views.review_list),
]