from django import forms
from django.contrib.auth.models import Group, User
from django.forms import FileInput, NumberInput, TextInput

from main_app.models import Favorite
from main_app.models import User as CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password_repeat = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password_repeat"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password_repeat"]

    def save(self, password, *, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(password)
            user.save()
            user_group = Group.objects.get(name="user")
            user_group.user_set.add(user)
            favorite = Favorite.objects.create()
            CustomUser.objects.create(
                name=user.username, surname="Smith", favorite=favorite, user_django=user
            )
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["name", "second_name", "surname", "age", "photo"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "second_name": TextInput(attrs={"class": "form-control"}),
            "surname": TextInput(attrs={"class": "form-control"}),
            "age": NumberInput(attrs={"class": "form-control", "min": 0}),
            "photo": FileInput(attrs={"class": "form-control form-control-lg"}),
        }


class ProfilePasswordForm(forms.ModelForm):
    username = forms.CharField(
        max_length=50,
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password_first = forms.CharField(
        label="Пароль",
        required=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "value": "", "placeholder": "password"}
        ),
    )
    password_repeat = forms.CharField(
        label="Повторите пароль",
        required=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "value": "", "placeholder": "password"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password_first", "password_repeat")

    def clean_password_repeat(self):
        cd = self.cleaned_data
        if cd["password_first"] != cd["password_repeat"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password_repeat"]
