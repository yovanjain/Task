from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Movie, Genres
from .serializer import MovieSerializer
from rest_framework.filters import SearchFilter


class MovieSearch(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','release_year','rating']

#Create your views here.
@api_view(['GET','POST','PUT', 'PATCH','DELETE'])
def MovieApi(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            movie = Movie.objects.get(id=id)
            serializer = MovieSerializer(movie)
            return Response(data= serializer.data, status= status.HTTP_200_OK)
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data= serializer.data, status= status.HTTP_200_OK)

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        id = pk
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        id = pk
        movie = Movie.objects.get(pk=id)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    if request.method == "DELETE":
        id = pk
        movie = Movie.objects.get(pk=id)
        movie.delete()
        return Response({'msg':'Data deleted successfully'})


    




    
    




