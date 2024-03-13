import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.db.models.signals import post_save
from django.dispatch import receiver
from icecream import ic

from main_app.models import Car, Motocycle, Service, User
from .views import create_image_preview
from django.core.mail import send_mail



@receiver(post_save, sender=Car)
def car_created(sender, instance, created, **kwargs):
    if created:
        create_image_preview(instance, 'car')
        ic(instance)

        # Определяем текст сообщения в зависимости от статуса пользователя
        all_users = User.objects.filter(groups__name='moder')
        user_emails = [user.email for user in all_users]



@receiver(post_save, sender=Motocycle)
def Motocycle_created(sender, instance, created, **kwargs):
    if created:
        create_image_preview(instance, 'moto')
        # Определяем текст сообщения в зависимости от статуса пользователя
        all_users = User.objects.filter(groups__name='moder')
        user_emails = [user.email for user in all_users]



@receiver(post_save, sender=Service)
def Service_created(sender, instance, created, **kwargs):
    if created:

        # Определяем текст сообщения в зависимости от статуса пользователя
        all_users = User.objects.filter(groups__name='moder')
        user_emails = [user.email for user in all_users]



@receiver(post_save, sender=User)
def User_created(sender, instance, created, **kwargs):
    if created:
        pass

