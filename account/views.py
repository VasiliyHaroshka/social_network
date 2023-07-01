from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import LoginForm, RegistrationForm


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
