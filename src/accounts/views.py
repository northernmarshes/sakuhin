from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """New user registration"""
    if request.method != "POST":
        # Displaying empty reqistration form
        form = UserCreationForm()
    else:
        # Processing a filled form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Loggin an user and redirecting to the main page
            login(request, new_user)
            return redirect("artworks:index")
    # Displaying an emptu form
    context = {"form": form}
    return render(
        request,
        "registration/register.html",
        context,
    )
