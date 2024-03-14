from django import forms
from django.forms import Textarea, FileInput, Select, NumberInput, TextInput, CheckboxInput, SelectMultiple, \
    PasswordInput, EmailInput
from django.contrib.auth.models import User as DjangoUser

from main_app.models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['guarantee', 'slug']
        widgets = {
            'brand': TextInput(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'cols': 4, 'rows': 3}),
            'photo': FileInput(attrs={'class': 'form-control form-control-lg'}),
            'color': Select(attrs={'class': 'form-select'}),
            'body_type': Select(attrs={'class': 'form-select'}),
            'drive_type': Select(attrs={'class': 'form-select'}),
            'engine_type': Select(attrs={'class': 'form-select'}),
            'guarantee_period': Select(attrs={'class': 'form-select'}),
            'distance': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'year_produced': TextInput(
                attrs={'type': 'range', 'class': 'form-range', 'min': 1990, 'max': 2024, 'steps': 1}),
            'price': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'engine_power': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'used_car': CheckboxInput(attrs={'class': 'form-check-input'}),
            'seller': Select(attrs={'class': 'form-select'}),
        }


class MotocycleForm(forms.ModelForm):
    class Meta:
        model = Motocycle
        exclude = ['guarantee', 'slug']
        widgets = {
            'brand': TextInput(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'cols': 4, 'rows': 3}),
            'photo': FileInput(attrs={'class': 'form-control form-control-lg'}),
            'color': Select(attrs={'class': 'form-select'}),
            'body_type': Select(attrs={'class': 'form-select'}),
            'engine_type': Select(attrs={'class': 'form-select'}),
            'guarantee_period': Select(attrs={'class': 'form-select'}),
            'distance': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'year_produced': TextInput(
                attrs={'type': 'range', 'class': 'form-range', 'min': 1990, 'max': 2024, 'steps': 1}),
            'price': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'engine_power': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'used_car': CheckboxInput(attrs={'class': 'form-check-input'}),
            'seller': Select(attrs={'class': 'form-select'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['guarantee', 'slug']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'cols': 4, 'rows': 3}),
            'photo': FileInput(attrs={'class': 'form-control form-control-lg'}),
            'guarantee_period': Select(attrs={'class': 'form-select'}),
            'price': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_available': CheckboxInput(attrs={'class': 'form-check-input'}),
            'cars_service': SelectMultiple(attrs={'class': 'form-select', 'size': 6}),
            'motorcycles_service': SelectMultiple(attrs={'class': 'form-select', 'size': 6}),
            'in_charge': Select(attrs={'class': 'form-select'}),
        }


class UserForm(forms.Form):
    choices = [
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор'),
    ]
    username = forms.CharField(max_length=50, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Новый пароль', required=False,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    group = forms.ChoiceField(label='Группа', initial='user', choices=choices,
                              widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('username', None)
        group = kwargs.pop('group', None)
        email = kwargs.pop('email', None)
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = username
        self.fields['group'].initial = group
        self.fields['email'].initial = email

