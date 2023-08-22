from django.urls import path

from .views import image_download, image_detail, image_like, image_list

urlpatterns = [
    path("", image_list, name="list"),
    path("download/", image_download, name="download"),
    path("<int:id>/<slug:slug>/", image_detail, name="detail"),
    path("like/", image_like, name="like"),
]
