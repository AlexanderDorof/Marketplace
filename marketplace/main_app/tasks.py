import time

from django.core.mail import send_mail, BadHeaderError
from celery.utils.log import get_task_logger

from marketplace.settings import DEFAULT_FROM_EMAIL
from marketplace.celery import app

logger = get_task_logger(__name__)


@app.task
def send_email_task(subject, message, RECIPIENT_EMAILS):
    print('task excepted:', subject)
    time.sleep(5)
    logger.info(f'from={DEFAULT_FROM_EMAIL}, {RECIPIENT_EMAILS=}, {subject=}, {message=}')
    try:
        logger.info('About to send_mail')
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [RECIPIENT_EMAILS])
    except BadHeaderError:
        logger.info('BadHeaderError')
    except Exception as e:
        logger.error(e)

    return 'message sent'
