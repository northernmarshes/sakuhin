from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm
# from .forms import ArtworkForm


@login_required
def books(request):
    books = Book.objects.filter(owner=request.user).order_by("created_at")
    context = {"books": books}
    return render(request, "books/books.html", context)


@login_required
def new_book(request):
    "Add new book"
    if request.method != "POST":
        # If empty creating a new form
        form = BookForm()
    else:
        # Else filling a form with POSTed data
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect("artworks:artworks")

    # Wyświetlanie pustego formularza
    context = {"form": form}
    print("USER:", request.user, request.user.is_authenticated)
    return render(request, "books/new_book.html", context)
