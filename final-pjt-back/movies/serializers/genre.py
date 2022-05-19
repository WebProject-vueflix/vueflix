from rest_framework import serializers
from ..models import Genre
from accounts.models import User

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre',)
