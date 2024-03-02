from django import forms
from main_app.models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class MotocycleForm(forms.ModelForm):
    class Meta:
        model = Motocycle
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'