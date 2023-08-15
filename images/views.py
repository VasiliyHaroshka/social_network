from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import ImageDownloadForm
from .models import Image


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


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
        "section": "images",
    }
    return render(request, "images/image/download.html", context)


def image_detail(request, id, slug):
    """Обработчик для редактирования сведений об изображении"""
    image = get_object_or_404(Image, id=id, slug=slug)
    context = {
        "image": image,
        "section": "images",
    }
    return render(request, "images/image/detail.html", context)


def image_list(request):
    """Обработчик постраничного отображения картинок
    через стандартный запрос и через ajax-запрос"""
    images = Image.objects.all()
    paginator = Paginator(images, 5)
    page = request.GET.get("page")
    try:
        images = paginator.page("page")
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        if is_ajax(request=request):
            return HttpResponse("")
        images = paginator.page(paginator.num_pages)

    context = {
        "images": images,
        "section": "images",
    }
    if is_ajax(request=request):
        return render(request, "images/image/list_ajax.html", context)
    return render(request, "images/image/list.html", context)


@login_required
@require_POST
def image_like(request):
    """Обработчик лайков на картинке"""
    image_id = request.POST.get("id")
    action = request.POST.get("action")

    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == "like":
                image.like.add(request.user)
            else:
                image.like.remove(request.user)
            return JsonResponse({"status": "ok"})
        except Exception:
            pass

    return JsonResponse({"status": "ok"})
