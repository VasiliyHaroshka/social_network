from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageDownloadForm
from .models import Image


@login_required
def image_download(request):
    """Отображает форму добавления картинки.
    Загружает картинку и привязывает её к пользователю"""
    if request.method == "POST":
        form = ImageDownloadForm(request.POST)
        if form.is_valid():
            new_picture = form.save(commit=False)
            new_picture.user = request.user
            new_picture.save()
            messages.success(request, "Image download successfully!")
            return redirect(new_picture.get_absolute_url())

    else:
        form = ImageDownloadForm(request.GET)

    context = {
        "form": form,
    }
    return render(request, "images/image/download.html", context)


def image_detail(request, id, slug):
    """Обработчик для редактирования сведений об изображении"""
    image = get_object_or_404(Image, id=id, slug=slug)
    context = {
        "image": image,
        # "section": images,
    }
    return render(request, "images/image/detail.html", context)
