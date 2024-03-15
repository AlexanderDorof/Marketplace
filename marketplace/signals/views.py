import os

from django.shortcuts import render
from django.contrib.auth.models import User as DjangoUser
from PIL import Image

from marketplace.settings import BASE_DIR


def create_image_preview(instance, model):
    img_url = instance.photo.url
    img_url = img_url[1:]
    full_path = os.path.join(BASE_DIR, img_url)
    image = Image.open(full_path)
    resized_image = image.resize((300, 200))
    rel = f'media/photos/{model}s/{model}s_previews/preview_image_{instance.pk}.jpg'
    img_path_new = os.path.join(BASE_DIR, rel)
    resized_image.save(img_path_new)
    instance.photo = f'/photos/{model}s/{model}s_previews/preview_image_{instance.pk}.jpg'
    instance.save()


def moders_emails():
    all_moders = DjangoUser.objects.filter(groups__name='moder')
    return [moder.email for moder in all_moders]


def admins_emails():
    all_admin = DjangoUser.objects.filter(groups__name='admin')
    return [admin.email for admin in all_admin]


def owner_email(instance):
    user = instance.seller
    django_user = user.user_django
    email = django_user.email
    return email


