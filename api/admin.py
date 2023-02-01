from django.contrib import admin
from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ["title", "active", "created_at", "updated_at"]
    list_editable = ["active"]
