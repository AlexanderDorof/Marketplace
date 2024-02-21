from django import template

register = template.Library()


@register.simple_tag()
def user_is_seller(seller, user):
    return seller == user