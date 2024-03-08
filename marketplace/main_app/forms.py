from django import forms
from django.forms import Textarea, FileInput, Select, NumberInput, Widget, TextInput

from .models import *


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['used_car', 'seller']
        widgets = {
            'brand': TextInput(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'cols': 4, 'rows': 3}),
            'photo': FileInput(attrs={'class': 'form-control form-control-lg'}),
            'color': Select(attrs={'class': 'form-select'}),
            'body_type': Select(attrs={'class': 'form-select'}),
            'drive_type': Select(attrs={'class': 'form-select'}),
            'engine_type': Select(attrs={'class': 'form-select'}),
            'distance': NumberInput(attrs={'class': 'form-control','min': 0}),
            'year_produced': TextInput(attrs={'type': 'range', 'class': 'form-range','min': 1990,'max': 2024, 'steps': 1}),
            'price': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'engine_power': NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.seller = self.initial.get('seller')  # adds user who created record in db as seller
        self.instance.used_car = self.initial.get('used_car')  # marks that car/moto is uses


class AddMotoForm(forms.ModelForm):
    class Meta:
        model = Motocycle
        exclude = ['used_car', 'seller']
        widgets = {
            'brand': TextInput(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control', 'cols': 4, 'rows': 3}),
            'photo': FileInput(attrs={'class': 'form-control form-control-lg'}),
            'color': Select(attrs={'class': 'form-select'}),
            'body_type': Select(attrs={'class': 'form-select'}),
            'engine_type': Select(attrs={'class': 'form-select'}),
            'distance': NumberInput(attrs={'class': 'form-control','min': 0}),
            'year_produced': TextInput(attrs={'type': 'range', 'class': 'form-range','min': 1990,'max': 2024, 'steps': 1}),
            'price': NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'engine_power': NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.seller = self.initial.get('seller')  # adds user who created record in db as seller
        self.instance.used_car = self.initial.get('used_car')  # marks that car/moto is uses
