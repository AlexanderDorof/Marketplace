from django import template
from icecream import ic

from main_app.models import *

register = template.Library()


@register.simple_tag()
def user_is_seller(seller, user):
    return seller == user


@register.filter
def model_name(obj):
    return obj._meta.model_name


@register.simple_tag
def in_favorite(obj, pk):

    item_type = obj._meta.model_name
    user = User.objects.get(user_django__pk=pk)
    if item_type == 'car':
        if user.favorite.favorite_cars.filter(pk=obj.pk).exists():
            return '/static_imgs/heart-icon.svg'
        else:
            return '/static_imgs/add-to-favorites-icon.svg'
    elif item_type == 'motocycle':
        if user.favorite.favorite_moto.filter(pk=obj.pk).exists():
            return '/static_imgs/heart-icon.svg'
        else:
            return '/static_imgs/add-to-favorites-icon.svg'
