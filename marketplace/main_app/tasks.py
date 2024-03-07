import time

from marketplace.celery import app
from celery.utils.log import get_task_logger

from django.core.mail import send_mail, BadHeaderError
from marketplace.settings import DEFAULT_FROM_EMAIL, recepient_email


logger = get_task_logger(__name__)
p = f'From: {DEFAULT_FROM_EMAIL}\nTo: {recepient_email}\nSubject: {123231}\n\ntest message'

@app.task(bind=True)
def send_email_task(self, message):
    print("task executed", message)
    time.sleep(5)
    print(logger)
    logger.info("About to send_mail")
    # send_mail('test subject', p, DEFAULT_FROM_EMAIL, [recepient_email], fail_silently=False)
    return "wonderful"
    # logger.info(f"from={DEFAULT_FROM_EMAIL}, {to=}, {subject=}, {message=}")
    # try:
    #     logger.info("About to send_mail")
    #     send_mail(subject, message, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
    # except BadHeaderError:
    #     logger.info("BadHeaderError")
    # except Exception as e:
    #     logger.error(e)