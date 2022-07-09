from rest_framework import serializers
from .models import Movie, Genres

class GenersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['id','title']

class MovieSerializer(serializers.ModelSerializer):
    genres= GenersSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id','title','release_year','rating', 'genres']
