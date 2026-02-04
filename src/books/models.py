from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, blank=True, verbose_name="Author")
    year = models.IntegerField(null=True, blank=True, verbose_name="Year")
    isbn = models.CharField(max_length=13, blank=True, verbose_name="ISBN")
    publisher = models.CharField(max_length=100, blank=True, verbose_name="Publisher")
    pages = models.IntegerField(null=True, blank=True, verbose_name="Pages")
    cover = models.ImageField(upload_to="books/%Y/%m/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.author}"
