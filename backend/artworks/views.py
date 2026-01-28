from django.shortcuts import render, redirect
from .models import Artwork
from .forms import ArtworkForm


def index(request):
    return render(request, "artworks/index.html")


def artworks(request):
    artworks = Artwork.objects.order_by("created_at")
    context = {"artworks": artworks}
    return render(request, "artworks/artworks.html", context)


def new_artwork(request):
    "Add new artwork"
    if request.method != "POST":
        # If empty creating a new form
        form = ArtworkForm()
    else:
        # Else filling a form with POSTed data
        form = ArtworkForm(data=request.POST)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.owner = request.user
            artwork.save()
            return redirect("artworks:artworks")

    # Wyświetlanie pustego formularza
    context = {"form": form}
    return render(request, "artworks/new_artwork.html", context)
