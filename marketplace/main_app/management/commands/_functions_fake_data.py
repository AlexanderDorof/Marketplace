import os
import random

from django.utils.text import slugify

from main_app.models import Car, Motocycle, User, Service
from ._fake_data import cars_brand_models, motors_brand_models, services_title
from marketplace.settings import BASE_DIR


def users_id():
    users = User.objects.all()
    return [user.id for user in users]


def insertcars(num=20, filename='cars_mini'):
    photo_cars_path = fr'{BASE_DIR}/media/photos/cars/{filename}'
    photo_cars = list(os.walk(photo_cars_path))[0][2]
    ColorsType = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'teal')

    for i in range(num):
        brand = random.choice(list(cars_brand_models.keys()))
        model = random.choice(cars_brand_models[brand])
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


def insertmotors(num=20, filename='motors'):
    photo_motors = list(os.walk(fr'{BASE_DIR}/media/photos/motos/{filename}'))[0][2]
    ColorsType = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'teal')
    for i in range(num):
        brands = list(motors_brand_models.keys())
        brand = random.choice(brands)
        model = random.choice(motors_brand_models[brand])
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


def insertservices(num=5):
    for i in range(num):
        in_charge = random.choice(('Смирнов И.И.', 'Сидоров А.К.', 'Петров Г.С.', 'Анохин Е.З.'))
        title = random.choice(services_title)
        is_available = random.choices((True, False), weights=[0.95, 0.05], k=1)[0]
        price = random.randint(5, 1_000)
        slug = f'{title}-{price}-{in_charge}'
        slug = slugify(slug)
        Service.objects.create(title=title, in_charge=in_charge, is_available=is_available,
                               slug=slug,
                               price=price)
