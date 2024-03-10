from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView

from main_app.models import User as CustomUser
from .forms import UserRegistrationForm, ProfileForm, ProfilePasswordForm
from main_app.utils import DataMixin
from .permissions import ProfilePermissionsMixin, PasswordPermissionsMixin


class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('register:login')

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


class UserEditProfileView(ProfilePermissionsMixin, DataMixin, UpdateView):
    model = CustomUser
    extra_context = {'title': 'Редактирование профиля'}
    form_class = ProfileForm
    template_name = 'register/profile.html'
    success_url = reverse_lazy('home')
    login_url = 'register:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context

class UserEditPasswordView(PasswordPermissionsMixin, DataMixin, UpdateView):
    model = User
    extra_context = {'title': 'Редактирование профиля'}
    form_class = ProfilePasswordForm
    template_name = 'register/profile.html'
    success_url = reverse_lazy('home')
    login_url = 'register:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context
