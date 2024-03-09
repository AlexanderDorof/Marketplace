from django import template
from django.db.models import Model

from main_app.models import *

register = template.Library()


@register.simple_tag()
def user_is_seller(seller: User, user: User) -> bool:
    """tag return true if user is seller"""
    return seller == user


@register.filter
def model_name(obj: Model) -> str:
    """tag retrun name of the model"""
    return obj._meta.model_name


@register.simple_tag
def in_favorite(obj: Model, pk: int) -> str:
    """tag return heart type whether item in favorite or not"""
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
