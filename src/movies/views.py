import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie
from django.contrib import messages
from .forms import MovieForm


@login_required
def movies(request):
    movies = Movie.objects.filter(owner=request.user).order_by("created_at")
    context = {"movies": movies}
    return render(request, "movies/movies.html", context)


@login_required
def new_movie(request):
    "Add new movie"
    if request.method != "POST":
        # If empty creating a new form
        form = MovieForm()
    else:
        # Else filling a form with POSTed data
        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            return redirect("movies:movies")

    # Wyświetlanie pustego formularza
    context = {"form": form}
    print("USER:", request.user, request.user.is_authenticated)
    return render(request, "movies/new_movie.html", context)


def movie_details(request, pk):
    movie = get_object_or_404(Movie, pk=pk, owner=request.user)
    context = {"movie": movie}
    return render(request, "movies/movie_details.html", context)


@login_required
def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method != "POST":
        form = MovieForm(instance=movie)
    else:
        form = MovieForm(instance=movie, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated successfully!")
            return redirect("books:books")

    context = {"form": form, "movie": movie}
    return render(request, "movies/edit_movie.html", context)


@login_required
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Movie deleted successfully!")
        return redirect("movies:movies")
    context = {"movies": movies}
    return render(request, "movies/movies.html", context)
