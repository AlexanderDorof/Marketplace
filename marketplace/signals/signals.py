# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from main_app.models import Car,Motocycle
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
#
# login = 'blackbloodyring@gmail.com'
# password = ''
# sender_email = login
# sender_password = password
#
# @receiver(post_save, sender=Car)
# def car_created(sender, instance, created, **kwargs):
#     if created:
#         # Создаем объект MIMEMultipart
#         message = MIMEMultipart()
#         message['From'] = sender_email
#
#         # Определяем текст сообщения в зависимости от статуса пользователя
#         all_users = User.objects.filter(groups__name='moder')
#         user_emails = [user.email for user in all_users]
#         print(user_emails)
#
#         # Добавляем тему и тело сообщения
#         message['Subject'] = 'Announcement Created'
#         message.attach(MIMEText('Announcement created for the car with details:\n\n{}'.format(instance), 'plain'))
#
#         # Добавляем адреса получателей
#         message['To'] = ', '.join(user_emails)
#
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.send_message(message)
#
# @receiver(post_save, sender=Motocycle)
# def Motocycle_created(sender, instance, created, **kwargs):
#     if created:
#         # Создаем объект MIMEMultipart
#         message = MIMEMultipart()
#         message['From'] = sender_email
#
#         # Определяем текст сообщения в зависимости от статуса пользователя
#         all_users = User.objects.filter(groups__name='moder')
#         user_emails = [user.email for user in all_users]
#         print(user_emails)
#
#         # Добавляем тему и тело сообщения
#         message['Subject'] = 'Announcement Created'
#         message.attach(MIMEText('Announcement created for the car with details:\n\n{}'.format(instance), 'plain'))
#
#         # Добавляем адреса получателей
#         message['To'] = ', '.join(user_emails)
#
#         with smtplib.SMTP('smtp.gmail.com', 587) as server:
#             server.starttls()
#             server.login(sender_email, sender_password)
#             server.send_message(message)
