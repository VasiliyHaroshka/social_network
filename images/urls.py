from django.urls import path

from .views import image_download, image_detail

urlpatterns = [
    path("download/", image_download, name="download"),
    path("detail/<int:id>/<slug:slug>/", image_detail, name="detail"),
]
