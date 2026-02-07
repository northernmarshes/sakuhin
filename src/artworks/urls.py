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
    # editing an artwork
    path("edit/<int:pk>/", views.edit_artwork, name="edit_artwork"),
    # deleting an artwork
    path("delete/<int:pk>/", views.delete_artwork, name="delete_artwork"),
    # artwork details
    path("/<int:pk>/", views.artwork_details, name="artwork_detail"),
]
