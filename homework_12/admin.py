from django.contrib import admin

from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "developer",
        "genre",
        "release_year",
        "price",
        "is_available",
        "created_at"
    )

    list_display_links = (
        "title",
        "developer"
    )

    list_editable = (
        "is_available",
        "price"
    )

    list_filter = (
        "genre",
        "release_year",
        "is_available",
        "created_at"
    )

    search_fields = (
        "title",
        "developer",
        "genre"
    )

    ordering = (
        "-release_year",
        "title"
    )

    list_per_page = 10

    fields = (
        "title",
        "developer",
        "genre",
        ("release_year", "price"),
        "description",
        "is_available"
    )