from django.shortcuts import get_object_or_404
from django.db.models import Count
from requests import request

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review, Comment
from .serializers.review import ReviewSerializer,ReviewListSerializer
from .serializers.comment import CommentSerializer

@api_view(['GET','POST'])
def review_list_or_create(request):

    def review_list():

        reviewlist = Review.objects.annotate(
            comment_count = Count('community_review', distinct=True)
        ).order_by('-pk')

        serealizer = ReviewListSerializer(reviewlist, many=True)
        return Response(serealizer.data)
    
    def create_review():

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()

@api_view(['GET','DELETE','PUT'])
def review_detail_or_delete_or_update(request, review_pk):
    #전체 공통되는 데이터 review 지정
    review = get_object_or_404(Review,pk=review_pk)
    # get 일 때 조회
    def detail_review():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    if request.method == 'GET':
        return detail_review()
    elif request.method == 'DELETE':
        return delete_review()
    elif request.method == 'PUT':
        return update_review()

# @api_view(['GET'])
# def comment_list():
#     reviewlist = Review.objects.annotate(
#         comment_count = Count('community_review', distinct=True)
#     ).order_by('-pk')

#     serealizer = ReviewListSerializer(reviewlist, many=True)
#     return Response(serealizer.data)

@api_view(['POST'])
def comment_create(request,review_pk):
    user = request.user

    review = get_object_or_404(Review,pk=review_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)

        comments = review.community_review.all()
        serealizer = CommentSerializer(comments, many=True)
        return Response(serealizer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
def comment_delete_or_update(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)


    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = review.community_review.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = review.community_review.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    if request.method == 'DELETE':
        return delete_comment()
    elif request.method == 'PUT':
        return update_comment()


