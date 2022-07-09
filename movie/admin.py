from django.contrib import admin
from .models import Movie, Genres
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','release_year','rating']

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    
