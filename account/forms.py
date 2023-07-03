from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    """Форма логирования"""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    """Форма регистрации"""
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(self):
        data = self.cleaned_data
        if data["password1"] != data["password2"]:
            raise forms.ValidationError("Password1 and password2 don't match!")
        return data["password2"]


class BaseUserEditForm(forms.ModelForm):
    """Форма редактирования стандартных данных пользователя"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class AddUserEditForm(forms.ModelForm):
    """Форма редактирования расширенных полей стандартной модели пользователя"""

    class Meta:
        model = Profile
        fields = ("birth_date", "photo")
