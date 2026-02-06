from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm


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
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect("books:books")

    # Wyświetlanie pustego formularza
    context = {"form": form}
    print("USER:", request.user, request.user.is_authenticated)
    return render(request, "books/new_book.html", context)


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method != "POST":
        form = BookForm(instance=book)
    else:
        form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("artworks:artworks")
    context = {"form": form, "book": book}
    return render(request, "books/edit_book.html", context)


@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect("books:books")
    context = {"books": books}
    return render(request, "books/books.html", context)
