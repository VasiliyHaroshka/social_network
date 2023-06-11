from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def show_dashboard(request):
    """Отображает рабочий стол аккаунта"""
    context = {
        "section": "dashboard",
    }
    return render(request, "account/dashboard.html", context)
