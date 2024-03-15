import os
import random

from django.db import IntegrityError
from django.utils.text import slugify
from django.utils import timezone

from main_app.models import Car, Motocycle, User, Service, ItemForCar, ItemForMotorcycle
from ._fake_data import CARS_BRAND_MODELS, MOTORS_BRAND_MODELS, SERVICES_TITLE, ITEMS_CARS, ITEMS_MOTORCYCLES
from marketplace.settings import BASE_DIR


def users_id():
    """Returns id of all users form custom model in main_app"""
    users = User.objects.all()
    return [user.id for user in users]


def russian_to_english_transliteration(russian_sentence):
    """Define a mapping of Russian letters to their English equivalents"""
    translit_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    return ''.join(translit_map.get(letter, letter) for letter in russian_sentence.lower())


def insert_cars(num=20, filename='cars_mini'):
    photo_cars_path = fr'{BASE_DIR}/media/photos/cars/{filename}'
    photo_cars = list(os.walk(photo_cars_path))[0][2]
    ColorsType = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'teal')

    for i in range(num):
        brand = random.choice(list(CARS_BRAND_MODELS.keys()))
        model = random.choice(CARS_BRAND_MODELS[brand])
        engine_type = random.choice(('Electricity', 'Oil'))
        color = random.choice(ColorsType)
        used_car = random.choices((True, False), weights=[0.8, 0.2], k=1)[0]
        year_produced = random.randint(1990, 2024)
        distance = random.randint(0, 100_000)
        engine_power = random.randint(1000, 5000)
        price = random.randint(5_000, 50_000)
        body_type = random.choice(('Sedan', 'Hatchback', 'Pickup', 'Cabrio'))
        drive_type = random.choice(('Front', 'Back', 'Full'))
        photo = fr'photos/cars/{filename}/{random.choice(photo_cars)}'
        slug = f'{brand}-{model}-{price}'
        slug = slugify(slug)
        Car.objects.create(brand=brand, model=model, color=color, body_type=body_type, drive_type=drive_type,
                           engine_type=engine_type, distance=distance, year_produced=year_produced,
                           engine_power=engine_power, slug=slug, used_car=used_car,
                           price=price, photo=photo, seller_id=random.choice(users_id()))


def insert_motors(num=20, filename='motors'):
    photo_motors = list(os.walk(fr'{BASE_DIR}/media/photos/motos/{filename}'))[0][2]
    ColorsType = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'teal')
    for i in range(num):
        brands = list(MOTORS_BRAND_MODELS.keys())
        brand = random.choice(brands)
        model = random.choice(MOTORS_BRAND_MODELS[brand])
        year_produced = random.randint(1990, 2024)
        engine_power = random.randint(1000, 5000)
        color = random.choice(ColorsType)
        used_car = random.choices((True, False), weights=[0.8, 0.2], k=1)[0]
        price = random.randint(5_000, 50_000)
        photo = fr'photos/motos/motors/{random.choice(photo_motors)}'
        slug = f'{brand}-{model}-{price}'
        slug = slugify(slug)
        Motocycle.objects.create(brand=brand, model=model, year_produced=year_produced,
                                 engine_power=engine_power, color=color, used_car=used_car,
                                 slug=slug,
                                 price=price, photo=photo, seller_id=random.choice(users_id()))


def insert_services(num=5):
    for i in range(num):
        in_charge = random.choice(('Смирнов И.И.', 'Сидоров А.К.', 'Петров Г.С.', 'Анохин Е.З.'))
        title = random.choice(SERVICES_TITLE)
        is_available = random.choices((True, False), weights=[0.95, 0.05], k=1)[0]
        price = random.randint(5, 1_000)
        slug = russian_to_english_transliteration(f'{title}-{price}-{in_charge}')
        slug = slugify(slug)
        Service.objects.create(title=title, in_charge=in_charge, is_available=is_available,
                               slug=slug,
                               price=price)


def insert_items_cars(num=5):
    unique_value = iter(range(num))
    for i in range(num):
        title = random.choice(list(ITEMS_CARS.keys()))
        description = ITEMS_CARS[title]
        is_available = random.choices((True, False), weights=[0.95, 0.05], k=1)[0]
        price = random.randint(5, 999)
        slug = russian_to_english_transliteration(f'{title}-{price}')
        slug = slugify(slug)
        try:
            ItemForCar.objects.create(title=title, description=description, is_available=is_available,
                                      slug=slug, price=price)
        except IntegrityError as e:
            slug += timezone.now().strftime('_%Y-%m-%d_time%H:%M:%S_')
            slug += str(next(unique_value))
            ItemForCar.objects.create(title=title, description=description, is_available=is_available,
                                      slug=slug, price=price)


def insert_items_motors(num=5):
    unique_value = iter(range(num))
    for i in range(num):
        title = random.choice(list(ITEMS_MOTORCYCLES.keys()))
        description = ITEMS_MOTORCYCLES[title]
        is_available = random.choices((True, False), weights=[0.95, 0.05], k=1)[0]
        price = random.randint(5, 999)
        slug = russian_to_english_transliteration(f'{title}-{price}')
        slug = slugify(slug)
        try:
            ItemForMotorcycle.objects.create(title=title, description=description, is_available=is_available,
                                             slug=slug, price=price)
        except IntegrityError as e:
            slug += timezone.now().strftime('_%Y-%m-%d_time%H:%M:%S_')
            slug += str(next(unique_value))
            ItemForMotorcycle.objects.create(title=title, description=description, is_available=is_available,
                                             slug=slug, price=price)
