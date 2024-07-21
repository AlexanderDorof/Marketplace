from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CustomCar(admin.ModelAdmin):
    list_display = ("brand", "model", "preview", "used_car", "year_produced", "price")
    prepopulated_fields = {"slug": ("brand", "model")}

    def preview(self, model_instance):
        """add previw photo in admin panel"""
        short_description = "Фото"
        return mark_safe(f"<img src='{model_instance.photo.url}' width=100 height=80>>")

    preview.short_description = "Фото"


class CustomMoto(admin.ModelAdmin):
    list_display = ("brand", "model", "preview", "used_car", "year_produced", "price")
    prepopulated_fields = {"slug": ("brand", "model")}

    def preview(self, model_instance):
        """add preview photo in admin panel"""
        return mark_safe(f"<img src='{model_instance.photo.url}' width=100 height=80>>")

    preview.short_description = "Фото"


class CustomItem(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CustomService(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "is_available")


admin.site.register(Car, CustomCar)
admin.site.register(Motocycle, CustomMoto)
admin.site.register(ItemForCar, CustomItem)
admin.site.register(ItemForMotorcycle, CustomItem)
admin.site.register(Service, CustomService)
admin.site.register(User)
admin.site.register(Favorite)
