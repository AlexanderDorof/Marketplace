import os

from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'us_cel.settings')

app = Celery('email_sender')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()