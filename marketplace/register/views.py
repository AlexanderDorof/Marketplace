from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from icecream import ic

from .forms import UserRegistrationForm
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.models import User
from icecream import ic
from main_app.models import User as CustomUser
from .utils import DataMixin




class RegisterView(FormView):

    form_class = UserRegistrationForm
    template_name = 'register/register.html'
    success_url = reverse_lazy("register:profile")

    def form_valid(self, form):
        password = form.cleaned_data['password']
        form.save(password=password)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    extra_context = {'title': 'Выход...'}
    template_name = 'register/logout.html'

class CustomLoginView(LoginView):
    extra_context = {'title': 'Войти на сайт'}
    template_name = 'register/login.html'

class UserEditProfileView(DataMixin, UpdateView):
    model = CustomUser
    extra_context = {'title': 'Редактирование профиля'}
    fields = "__all__" # Поля, которые вы хотите редактировать
    template_name = 'register/profile.html'  # Шаблон для редактирования машины
    success_url = reverse_lazy('home')  # URL-адрес для перенаправления после успешного редактирования

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context
