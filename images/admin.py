from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "description", "url", "created", "user")
    list_filter = ("title", "created", "user")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}

