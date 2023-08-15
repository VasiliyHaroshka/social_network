from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from .forms import LoginForm, RegistrationForm, BaseUserEditForm, AddUserEditForm
from .models import Profile, Contact


@login_required
def show_dashboard(request):
    """Отображает рабочий стол аккаунта"""
    context = {
        "section": "dashboard",
    }
    return render(request, "account/dashboard.html", context)


def registration(request):
    """Обработчик регистрации пользователя"""
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password1"])
            Profile.objects.create(user=new_user)
            new_user.save()

            context = {
                "new_user": new_user,
            }

            return render(request, "account/registration_done.html", context)

    else:
        form = RegistrationForm()
        context = {
            "form": form,
        }
        return render(request, "account/registration.html", context)


@login_required
def edit_profile(request):
    """Обработчик редактирования профиля пользователя"""
    if request.method == "POST":
        base_form = BaseUserEditForm(
            instance=request.user,
            data=request.POST,
        )
        add_form = AddUserEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES,
        )

        if base_form.is_valid() and add_form.is_valid():
            base_form.save()
            add_form.save()
            messages.success(request, "Profile was changed successfully!")
        else:
            messages.error(request, "There was something wrong! Try again.")

    else:
        base_form = BaseUserEditForm(instance=request.user)
        add_form = AddUserEditForm(instance=request.user.profile)

    context = {
        "base_form": base_form,
        "add_form": add_form,
    }

    return render(request, "account/edit_profile.html", context)


def user_list(request):
    """Отображение списка всех пользователей"""
    users = User.objects.filter(is_active=True)
    context = {
        "section": "people",
        "users": users,
    }
    return render(request, "account/user/list.html", context)


def user_detail(request, username):
    """Отображение конкретного пользователя"""
    user = get_object_or_404(User, username=username, is_active=True)
    context = {
        "section": "people",
        "user": user,
    }
    return render(request, "account/user/detail.html", context)


@require_POST
@login_required
def user_follow(request):
    """Обработчик подписки на других пользователей"""
    user_id = request.POST.get("id")
    action = request.POST.get("action")
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == "follow":
                Contact.objects.get_or_create(subscribed_from_user=request.user, subscribed_to_user=user)
            else:
                Contact.objects.filter(subscribed_from_user=request.user, subscribed_to_user=user).delete()
            return JsonResponse({"status": "ok"})
        except User.DoesNotExist:
            return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "ok"})
