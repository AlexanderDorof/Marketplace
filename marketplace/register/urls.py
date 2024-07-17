from django.urls import path

from .views import (
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
    UserEditPasswordView,
    UserEditProfileView,
)

app_name = "register"

urlpatterns = [
    path("profile/<int:pk>/", UserEditProfileView.as_view(), name="profile"),
    path(
        "change_password/<int:pk>/",
        UserEditPasswordView.as_view(),
        name="profile-password",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
