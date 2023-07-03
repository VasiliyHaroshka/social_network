from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import LoginForm, RegistrationForm, BaseUserEditForm, AddUserEditForm
from .models import Profile


@login_required
def show_dashboard(request):
    """Отображает рабочий стол аккаунта"""
    context = {
        "section": "dashboard",
    }
    return render(request, "account/dashboard.html", context)


def registration(request):
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

    else:
        base_form = BaseUserEditForm(instance=request.user)
        add_form = AddUserEditForm(instance=request.user.profile)

    context = {
        "base_form": base_form,
        "add_form": add_form,
    }

    return render(request, "account/edit_profile.html", context)