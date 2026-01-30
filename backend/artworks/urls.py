from django.urls import path
from . import views

app_name = "artworks"
urlpatterns = [
    # mainpage
    path("", views.index, name="index"),
    # artworks list
    path("artworks/", views.artworks, name="artworks"),
    # new artwork
    path("new_artwork/", views.new_artwork, name="new_artwork"),
]
