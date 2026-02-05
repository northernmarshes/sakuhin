from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            "title",
            "director",
            "year",
            "genre",
            "duration",
            "poster",
        ]
        widgets = {
            "year": forms.NumberInput(attrs={"min": 1888, "max": 2100}),
            "duration": forms.NumberInput(attrs={"min": 1}),
        }
