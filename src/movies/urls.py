from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    # movies list
    path("", views.movies, name="movies"),
    # new movie
    path("new_movie/", views.new_movie, name="new_movie"),
]
