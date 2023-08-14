from django.contrib import admin
from .models import Profile, Contact


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "birth_date", "photo")


@admin.register(Contact)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("subscribed_from_user", "subscribed_to_user", "created")
