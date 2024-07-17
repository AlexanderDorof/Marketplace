from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView

from main_app.models import User as CustomUser
from main_app.utils import DataMixin

from .forms import ProfileForm, ProfilePasswordForm, UserRegistrationForm
from .permissions import PasswordPermissionsMixin, ProfilePermissionsMixin


class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = "register/register.html"
    success_url = reverse_lazy("register:login")

    def form_valid(self, form):
        password = form.cleaned_data["password"]
        form.save(password=password)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    extra_context = {"title": "Выход..."}
    template_name = "register/logout.html"


class CustomLoginView(LoginView):
    extra_context = {"title": "Войти на сайт"}
    template_name = "register/login.html"


class UserEditProfileView(ProfilePermissionsMixin, DataMixin, UpdateView):
    model = CustomUser
    extra_context = {"title": "Редактирование профиля", "password": True}
    form_class = ProfileForm
    template_name = "register/profile.html"
    success_url = reverse_lazy("home")
    login_url = "register:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context


class UserEditPasswordView(PasswordPermissionsMixin, DataMixin, UpdateView):
    model = User
    extra_context = {"title": "Сменить пароль", "password": False}
    form_class = ProfilePasswordForm
    template_name = "register/profile.html"
    success_url = reverse_lazy("register:login")
    login_url = "register:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context = {**context, **c_def}
        return context

    def form_valid(self, form):
        new_username = form.cleaned_data["username"]
        password = form.cleaned_data["password_first"]
        user = self.request.user
        if new_username != user.username:
            user.username = new_username
        if password:
            user.set_password(password)
        user.save()
        return super().form_valid(form)
