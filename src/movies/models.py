from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies")
    poster = models.ImageField(upload_to="movies/%Y/%m/", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Title")
    director = models.CharField(max_length=100, blank=True, verbose_name="Director")
    year = models.IntegerField(null=True, blank=True, verbose_name="Year")
    genre = models.CharField(max_length=100, blank=True, verbose_name="Genre")
    duration = models.IntegerField(null=True, blank=True, verbose_name="Duration (min)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.year})"
