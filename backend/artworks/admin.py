from django.contrib import admin
from .models import Artwork


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "artist",
        "year",
        "medium",
        "owner",
        "created_at",
    ]
    list_filter = [
        "year",
        "medium",
        "artist",
        "created_at",
    ]
    search_fields = [
        "title",
        "artist",
        "medium",
        "discription",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]

    fieldsets = (
        ("Basic info", {"fields": ("title", "artist", "year")}),
        ("Details", {"fields": ("medium", "dimensions", "discription", "image")}),
        ("Owner", {"fields": ("owner",)}),
        (
            "Metadata",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
