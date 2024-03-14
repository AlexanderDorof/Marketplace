import time
import smtplib as smtp

from django.core.mail import send_mail, BadHeaderError
from celery.utils.log import get_task_logger

from marketplace.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT
from marketplace.celery import app

logger = get_task_logger(__name__)


@app.task
def send_email_task(subject, message, RECIPIENT_EMAILS):
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


@app.task
def send_email_task_smtp(subject, email_text, recipient_email):
    login_email = DEFAULT_FROM_EMAIL
    password = EMAIL_HOST_PASSWORD

    server = smtp.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    server.login(login_email, password)

    message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (login_email, recipient_email, subject, email_text)
    logger.info(f'from={DEFAULT_FROM_EMAIL}, {recipient_email=}, {subject=}, {message=}')
    time.sleep(5)
    try:
        logger.info('About to send_mail')
        server.sendmail(login_email, login_email, message)
    except BadHeaderError:
        logger.info('BadHeaderError')
    except Exception as e:
        logger.error(e)
    server.quit()
    return 'message sent'
