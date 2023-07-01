from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
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
