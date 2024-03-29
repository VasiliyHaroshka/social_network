from django.urls import path
from django.contrib.auth import views as auth_views

from .views import show_dashboard, registration, edit_profile, user_list, user_detail, user_follow

app_name = "account"

urlpatterns = [
    path("", show_dashboard, name="dashboard"),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("registration/", registration, name="registration"),

    path("edit_profile/", edit_profile, name="edit_profile"),

    path("user/", user_list, name="user_list"),
    path("user/follow/", user_follow, name="user_follow"),
    path("user/<username>/", user_detail, name="user_detail"),
]
