import os

from django.core.management.base import BaseCommand
import django

from ._functions_fake_data import insertcars, insertmotors, insertservices


class Command(BaseCommand):
    help = 'Creates db based on your data.'

    def handle(self, *args, **kwargs):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
        django.setup()

        cars_amount = 500
        motors_amount = 200
        services_amount = 60
        insertcars(num=cars_amount)
        insertmotors(num=motors_amount)
        insertservices(num=services_amount)

        self.stdout.write(self.style.SUCCESS(
            f'Default db with {cars_amount} cars, {motors_amount} motorcycles and {services_amount} services '
            f'created'))
