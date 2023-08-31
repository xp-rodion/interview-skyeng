from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.mixins import TitleMixin
from users.models import User
from users.forms import UserLoginForm, UserRegisterForm


class UserLoginView(LoginView):
    template_name = 'templates/login.html'
    form_class = UserLoginForm
    title = 'Вход'


class UserRegistrateView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'templates/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = f'Вы успешно зарегистрированы!'
    title = 'Регистрация'
