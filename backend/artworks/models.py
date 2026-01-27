from django.db import models
from django.contrib.auth.models import User


class Artwork(models.Model):
    """Model of an artwork"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="artworks",
        help_text="owner",
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Title",
        # help_text="title",
    )

    artist = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name="Artist",
        # help_text="artist",
    )

    year = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Year",
        # help_text="year",
    )

    medium = models.CharField(
        max_length=200,
        verbose_name="Medium",
        # help_text="medium",
    )

    dimensions = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Size",
        # help_text="size",
    )

    discription = models.TextField(
        blank=True,
        verbose_name="discription",
        # help_text="additional discription",
    )

    image = models.ImageField(
        upload_to="artworks/%Y/%m/",
        null=True,
        blank=True,
        verbose_name="image",
        # help_text="artwork image",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="creation date",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="last edited",
    )

    class Meta:
        verbose_name = "Artwork"
        verbose_name_plural = "Artworks"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.artist}"
