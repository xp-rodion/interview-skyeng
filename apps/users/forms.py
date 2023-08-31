from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm)

from users.models import User


class UserLoginForm(AuthenticationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите email пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':  'form-control py-4', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')