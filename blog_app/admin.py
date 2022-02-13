from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "status", "author", "published_at"]
    list_filter = ["status", "published_at", "created_at", "author"]
    search_fields = ["title", "content"]
    ordering = ["status", "published_at"]
    # auto_completefield=['author']
    autocomplete_fields = ["author"]
