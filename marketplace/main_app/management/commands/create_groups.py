from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
import os
import django

class Command(BaseCommand):
    help = 'Create default user groups'

    def handle(self, *args, **kwargs):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
        django.setup()

        # Создание групп пользователей
        Group.objects.get_or_create(name='user')
        Group.objects.get_or_create(name='moderator')
        Group.objects.get_or_create(name='admin')

        self.stdout.write(self.style.SUCCESS('Default user groups created successfully'))
