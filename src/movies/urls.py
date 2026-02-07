from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    # movies list
    path("", views.movies, name="movies"),
    # new movie
    path("new_movie/", views.new_movie, name="new_movie"),
    # edit a movie
    path("edit/<int:pk>/", views.edit_movie, name="edit_movie"),
    # delete a movie
    path("delete/<int:pk>/", views.delete_movie, name="delete_movie"),
    # movie details
    path("/<int:pk>/", views.movie_details, name="movie_details"),
]
