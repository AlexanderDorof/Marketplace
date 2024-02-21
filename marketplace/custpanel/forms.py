from django import forms
from main_app.models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

