from django.contrib.auth.models import User as DjangoUser
from django.db.models.signals import post_delete, post_save, pre_delete
from django.dispatch import receiver

from main_app.models import Car, Motocycle, Service, User
from main_app.tasks import send_email_task, send_email_task_smtp

from .views import admins_emails, create_image_preview, moders_emails, owner_email


@receiver(post_save, sender=Car)
def car_created(sender, instance, created, **kwargs):
    if created:
        create_image_preview(instance, "car")
        emails = moders_emails()


@receiver(post_save, sender=Motocycle)
def motorcycle_created(sender, instance, created, **kwargs):
    if created:
        create_image_preview(instance, "motor")
        emails = moders_emails()


@receiver(post_delete, sender=User)
def user_deleted(sender, instance, **kwargs):
    fav = instance.favorite
    fav.delete()


@receiver(pre_delete, sender=DjangoUser)
def django_user_deleted(sender, instance, **kwargs):
    email = owner_email(instance)
    message = f"We are sorry to inform you, but your account was deleted: {instance}"


@receiver(post_delete, sender=Car)
def car_deleted(sender, instance, **kwargs):
    email = owner_email(instance)
    subject = "Deletion..."
    message = f"Your car was deleted: {instance}"
    recipient_emails = "aleksandar.dorofeichik@yandex.ru"
    send_email_task_smtp.delay(subject, message, recipient_emails)


@receiver(post_delete, sender=Motocycle)
def motorcycle_deleted(sender, instance, **kwargs):
    email = owner_email(instance)
    message = f"Your motorcycle was deleted: {instance}"


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        emails = admins_emails()
        message = f"New user added: {instance}"
