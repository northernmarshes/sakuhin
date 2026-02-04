from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie
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
        form = MovieForm(data=request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            return redirect("movies:movies")

    # Wyświetlanie pustego formularza
    context = {"form": form}
    print("USER:", request.user, request.user.is_authenticated)
    return render(request, "movies/new_movie.html", context)
