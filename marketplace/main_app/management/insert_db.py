import os
import random
from django.utils.text import slugify

from django.http import HttpResponse
from icecream import ic

from main_app.models import Car, Motocycle

cars_brand_models = {
    "Toyota": ["Camry", "Corolla", "RAV4", "Highlander", "Tacoma", "Sienna", "Prius", "C-HR", "4Runner",
               "Land Cruiser"],
    "Volkswagen": ["Golf", "Passat", "Tiguan", "Jetta", "Atlas", "Arteon", "Golf GTI", "Touareg", "ID.4", "T-Cross"],
    "Ford": ["F-150", "Mustang", "Escape", "Explorer", "Ranger", "Edge", "Fusion", "Focus", "Expedition", "Bronco"],
    "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Odyssey", "HR-V", "Ridgeline", "Passport", "Crosstour", "Fit"],
    "Chevrolet": ["Silverado", "Equinox", "Tahoe", "Camaro", "Traverse", "Malibu", "Suburban", "Impala", "Blazer",
                  "Spark"],
    "Nissan": ["Altima", "Rogue", "Sentra", "Pathfinder", "Maxima", "Murano", "Frontier", "Titan", "Armada", "Leaf"],
    "BMW": ["3 Series", "5 Series", "X3", "X5", "7 Series", "X1", "X7", "4 Series", "2 Series", "i3"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLC", "GLE", "A-Class", "S-Class", "GLA", "GLB", "CLA", "GLS"],
    "Audi": ["A4", "Q5", "A3", "Q7", "A6", "Q3", "A5", "Q8", "TT", "e-tron"],
    "Hyundai": ["Elantra", "Tucson", "Sonata", "Santa Fe", "Kona", "Palisade", "Veloster", "Accent", "Venue", "IONIQ"]
}
motos_brand_models = {
    'Honda': ['Honda CB Shine', 'Honda Activa', 'Honda CBR 250RR', 'Honda CRF 250L', 'Honda Rebel 500',
              'Honda Africa Twin', 'Honda CB650R', 'Honda CB1000R', 'Honda Gold Wing', 'Honda Fireblade (CBR1000RR)'],
    'Yamaha': ['Yamaha YZF-R15', 'Yamaha MT-15', 'Yamaha FZ-S', 'Yamaha FZ25', 'Yamaha R3', 'Yamaha FZ16', 'Yamaha R1',
               'Yamaha XTZ 125', 'Yamaha XSR155', 'Yamaha Tracer 900'],
    'Suzuki': ['Suzuki Hayabusa', 'Suzuki Gixxer SF', 'Suzuki Intruder', 'Suzuki V-Strom 650', 'Suzuki GSX-S750',
               'Suzuki Access 125', 'Suzuki Burgman Street', 'Suzuki RM-Z450', 'Suzuki DR-Z400S', 'Suzuki SV650'],
    'Kawasaki': ['Kawasaki Ninja 300', 'Kawasaki Z650', 'Kawasaki Versys 650', 'Kawasaki Vulcan S',
                 'Kawasaki Ninja ZX-10R', 'Kawasaki KLX 140G', 'Kawasaki W800', 'Kawasaki Z900RS', 'Kawasaki KX450',
                 'Kawasaki Z400'],
    'Harley-Davidson': ['Harley-Davidson Street 750', 'Harley-Davidson Iron 883', 'Harley-Davidson Fat Boy',
                        'Harley-Davidson Road Glide', 'Harley-Davidson Sportster 1200', 'Harley-Davidson Softail Slim',
                        'Harley-Davidson Electra Glide', 'Harley-Davidson Low Rider', 'Harley-Davidson Breakout',
                        'Harley-Davidson LiveWire (Electric)'],
    'Ducati': ['Ducati Panigale V4', 'Ducati Monster 821', 'Ducati Scrambler', 'Ducati Diavel',
               'Ducati Multistrada 950', 'Ducati Hypermotard', 'Ducati SuperSport', 'Ducati Streetfighter V4',
               'Ducati 1299 Panigale', 'Ducati XDiavel'],
    'BMW Motorrad': ['BMW S 1000 RR', 'BMW R 1250 GS', 'BMW F 850 GS', 'BMW G 310 GS', 'BMW R nineT', 'BMW K 1600 GTL',
                     'BMW S 1000 XR', 'BMW F 900 R', 'BMW R 18', 'BMW G 310 R']}

photo_cars = next(os.walk(r'C:\Users\Alexander\Desktop\Project MarketPlace\Marketplace\photo_cars'))[2]
photo_motos = next(os.walk(r'C:\Users\Alexander\Desktop\Project MarketPlace\Marketplace\photo_motocycles'))[2]


def insertcars(requests):
    for i in range(50):
        brands = list(cars_brand_models.keys())
        brand = random.choice(brands)
        model = random.choice(cars_brand_models[brand])
        engine_type = random.choice(('Electricity', 'Oil'))
        year_produced = random.randint(1990, 2024)
        distance = random.randint(0, 100_000)
        engine_power = random.randint(1000, 5000)
        price = random.randint(5_000, 50_000)
        body_type = random.choice(('Sedan', 'Hatchback', 'Pickup', 'Cabrio'))
        drive_type = random.choice(('Front', 'Back', 'Full'))
        photo = fr'photos/cars/2024/03/01/{random.choice(photo_cars)}'
        slug = f'{brand}-{model}-{price}'
        slug = slugify(slug)
        Car.objects.create(brand=brand, model=model, body_type=body_type, drive_type=drive_type,
                           engine_type=engine_type, distance=distance, year_produced=year_produced,
                           engine_power=engine_power, slug=slug,
                           price=price, photo=photo, seller_id=1)
    return HttpResponse('Hello world')


def insertmotos(requests):
    for i in range(50):
        brands = list(motos_brand_models.keys())
        brand = random.choice(brands)
        model = random.choice(motos_brand_models[brand])
        year_produced = random.randint(1990, 2024)
        engine_power = random.randint(1000, 5000)
        price = random.randint(5_000, 50_000)
        photo = fr'photos/motos/2024/03/01/{random.choice(photo_motos)}'
        ic(photo_motos)
        slug = f'{brand}-{model}-{price}'
        slug = slugify(slug)
        Motocycle.objects.create(brand=brand, model=model, year_produced=year_produced, engine_power=engine_power,
                                 slug=slug,
                                 price=price, photo=photo, seller_id=1)
    return HttpResponse('Hello world')
