from django.urls import path
from . import views
# Create your views here.
app_name = 'community'

urlpatterns = [
    #review list
    #review create
    path('', views.review_list_or_create),
    
    #review detail/delete/update
    path('<int:review_pk>/', views.review_detail_or_delete_or_update),
    #commentlist

    #comment create
    path('<int:review_pk>/comments/', views.comment_create),
    #comment delete/update
    path('<int:review_pk>/comments/<int:comment_pk>', views.comment_delete_or_update)
]