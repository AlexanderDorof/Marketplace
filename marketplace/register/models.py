from django.contrib.auth.models import AbstractUser
from django.db import models


class Buyer(AbstractUser):
    ...


Buyer._meta.get_field('groups').remote_field.related_name = 'buyer_groups'
Buyer._meta.get_field('user_permissions').remote_field.related_name = 'buyer_user_permissions'
