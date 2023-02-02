from django.contrib import admin
from .models import Story, Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]
    search_fields = ["name", "code"]


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "created_at", "updated_at"]
    autocomplete_fields = ["language"]
    list_editable = ["active"]
