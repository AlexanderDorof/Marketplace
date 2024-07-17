import os

import django
from django.core.management.base import BaseCommand

from ._functions_fake_data import (
    insert_cars,
    insert_items_cars,
    insert_items_motors,
    insert_motors,
    insert_services,
)


class Command(BaseCommand):
    help = "Creates db based on your data."

    def handle(self, *args, **kwargs):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "marketplace.settings")
        django.setup()

        cars_amount = 0
        motors_amount = 0
        services_amount = 0
        items_cars = 0
        items_motors = 0
        insert_cars(num=cars_amount)
        insert_motors(num=motors_amount)
        insert_services(num=services_amount)
        insert_items_cars(num=items_cars)
        insert_items_motors(num=items_motors)

        self.stdout.write(
            self.style.SUCCESS(
                f"Default db with\n"
                f"{cars_amount} cars,\n"
                f"{motors_amount} motorcycles,\n"
                f"{services_amount} services,\n"
                f"{items_cars} car items,\n"
                f"{items_motors} motorcycle items\n"
                f"created"
            )
        )
