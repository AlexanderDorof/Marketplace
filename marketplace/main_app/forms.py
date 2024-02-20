from django import forms
from django.forms import Textarea
from icecream import ic

from .models import *


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ["used_car", 'seller']
        widgets = {
            "description ": Textarea(attrs={"cols": 40, "rows": 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.seller = self.initial.get('seller')
        self.instance.used_car = self.initial.get('used_car')




class AddMotoForm(forms.ModelForm):
    class Meta:
        model = Motocycle
        exclude = ["used_car", 'seller']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.seller = self.initial.get('seller')
        self.instance.used_car = self.initial.get('used_car')