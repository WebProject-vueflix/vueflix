from rest_framework import serializers
from ..models import Director
from accounts.models import User

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'profile_path',)
