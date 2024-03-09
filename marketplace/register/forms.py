from django import forms
from django.contrib.auth.models import User, Group
from django.forms import FileInput, NumberInput, TextInput

from main_app.models import User as CustomUser
from main_app.models import Favorite


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, password, *, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(password)
            user.save()
            user_group = Group.objects.get(name='user')
            user_group.user_set.add(user)
            favorite = Favorite.objects.create()
            CustomUser.objects.create(name=user.username, surname='Smith', favorite=favorite, user_django=user)
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'second_name', 'surname', 'age', 'photo']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'second_name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'age': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'photo': FileInput(attrs={'class': 'form-control form-control-lg'}),
        }
