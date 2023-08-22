from django.contrib import admin

from .models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ("user", "act", "target", "time")
    list_filter = ("time",)
    search_fields = ("act",)
