from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    # books list
    path("", views.books, name="books"),
    # new book
    path("new_book/", views.new_book, name="new_book"),
    # editing a book
    path("edit/<int:pk>/", views.edit_book, name="edit_book"),
    # deleting a book
    path("delete/<int:pk>/", views.delete_book, name="delete_book"),
    # book details
    path("/<int:pk>/", views.book_details, name="book_details"),
]
