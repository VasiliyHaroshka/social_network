from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def login_user(request):
    """Обработчик логирования пользователя"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data["username"],
                password=data["password"],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("You were authenticated successfully")
                else:
                    return HttpResponse("This account isn't active")
        else:
            return HttpResponse("Invalid data from the form")
    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, "account/login.html", context)
