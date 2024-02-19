from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CustomCar(admin.ModelAdmin):
    list_display = ('brand', "model", 'preview', 'used_car', "year_produced", "price")

    def preview(self, model_instance):
        return mark_safe(f"<img src='{model_instance.photo.url}' width=100 height=80>>")

    preview.short_description = "Фото"


class CustomMoto(admin.ModelAdmin):
    list_display = ('brand', "model", 'preview', 'used_car', "year_produced", "price")

    def preview(self, model_instance):
        return mark_safe(f"<img src='{model_instance.photo.url}' width=100 height=80>>")

    preview.short_description = "Фото"


admin.site.register(Car, CustomCar)
admin.site.register(Motocycle, CustomMoto)
admin.site.register(Item_for_car)
admin.site.register(Item_for_moto)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(Favorite)
