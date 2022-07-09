from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie_api/', views.MovieApi),
    path('movie_api/<int:pk>', views.MovieApi),
    path('movie_search/', views.MovieSearch.as_view()),
]
