from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    # books list
    path("", views.books, name="books"),
]
