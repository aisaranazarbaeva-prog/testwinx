from django.contrib import admin

from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "fairy",
        "score",
        "created_at",
    )
    list_filter = (
        "fairy",
        "created_at",
    )
    search_fields = (
        "user__username",
        "fairy__name",
    )