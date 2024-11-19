from django import forms
from .models import Admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['username','email','password1','password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Admin
        fields = ['email','password']







