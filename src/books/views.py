from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book
# from .forms import ArtworkForm


@login_required
def books(request):
    books = Book.objects.filter(owner=request.user).order_by("created_at")
    context = {"books": books}
    return render(request, "books/books.html", context)


# Create your views here.
