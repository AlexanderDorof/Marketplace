import os

from django.shortcuts import render
from PIL import Image

from marketplace.settings import BASE_DIR

def create_image_preview(instance, model):
    img_url = instance.photo.url
    img_url = img_url[1:]
    full_path = os.path.join(BASE_DIR, img_url)
    image = Image.open(full_path)
    resized_image = image.resize((300, 200))
    rel = f'media/photos/{model}s/{model}_previews/preview_image_{instance.pk}.jpg'
    img_path_new = os.path.join(BASE_DIR, rel)
    resized_image.save(img_path_new)
    instance.photo = f'/photos/{model}s/{model}_previews/preview_image_{instance.pk}.jpg'
    instance.save()
