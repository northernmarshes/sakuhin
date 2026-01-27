from django.urls import path
from . import views

app_name = "artworks"
urlpatterns = [
    # Mainpage
    path("", views.index, name="index"),
    # Artworks list
    path("artworks/", views.artworks, name="artworks"),
    # New artwork
    path("new_artwork/", views.new_artwork, name="new_artwork"),
]
