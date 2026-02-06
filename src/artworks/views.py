from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Artwork
from .forms import ArtworkForm


def index(request):
    return render(request, "artworks/index.html")


@login_required
def artworks(request):
    artworks = Artwork.objects.filter(owner=request.user).order_by("created_at")
    context = {"artworks": artworks}
    return render(request, "artworks/artworks.html", context)


@login_required
def new_artwork(request):
    "Add new artwork"
    if request.method != "POST":
        # If empty creating a new form
        form = ArtworkForm()
    else:
        # Else filling a form with POSTed data
        form = ArtworkForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.owner = request.user
            artwork.save()
            return redirect("artworks:artworks")

    # Wyświetlanie pustego formularza
    context = {"form": form}
    print("USER:", request.user, request.user.is_authenticated)
    return render(request, "artworks/new_artwork.html", context)


@login_required
def edit_artwork(request, pk):
    """Edit an artwork"""
    artwork = get_object_or_404(Artwork, pk=pk, owner=request.user)
    if request.method != "POST":
        form = ArtworkForm(instance=artwork)
    else:
        form = ArtworkForm(instance=artwork, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Artwork updated successfully!")
            return redirect("books:books")
    context = {"form": form, "artwork": artwork}
    return render(request, "artworks/edit_artwork.html", context)


@login_required
def delete_artwork(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    if request.method == "POST":
        artwork.delete()
        messages.success(request, "artwork deleted successfully!")
        return redirect("artworks:artworks")
    context = {"artworks": artworks}
    return render(request, "artworks/artworks.html", context)
