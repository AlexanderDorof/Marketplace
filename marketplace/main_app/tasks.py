import smtplib as smtp
import time

from celery.utils.log import get_task_logger
from django.core.mail import BadHeaderError, send_mail

from marketplace.celery import app
from marketplace.settings import (
    DEFAULT_FROM_EMAIL,
    EMAIL_HOST,
    EMAIL_HOST_PASSWORD,
    EMAIL_PORT,
)

logger = get_task_logger(__name__)


@app.task
def send_email_task(subject, message, RECIPIENT_EMAILS):
    """sends email using built in django send_mail method"""
    time.sleep(5)
    logger.info(
        f"from={DEFAULT_FROM_EMAIL}, {RECIPIENT_EMAILS=}, {subject=}, {message=}"
    )
    try:
        logger.info("About to send_mail")
        send_mail(subject, message, DEFAULT_FROM_EMAIL, [RECIPIENT_EMAILS])
    except BadHeaderError:
        logger.info("BadHeaderError")
    except Exception as e:
        logger.error(e)

    return "message sent"


@app.task
def send_email_task_smtp(subject, email_text, recipient_email):
    """sends email using built-in python smtp module"""
    login_email = DEFAULT_FROM_EMAIL
    password = EMAIL_HOST_PASSWORD

    server = smtp.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    server.login(login_email, password)

    message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (
        login_email,
        recipient_email,
        subject,
        email_text,
    )
    logger.info(
        f"from={DEFAULT_FROM_EMAIL}, {recipient_email=}, {subject=}, {message=}"
    )
    time.sleep(5)
    try:
        logger.info("About to send_mail")
        server.sendmail(login_email, login_email, message)
    except BadHeaderError:
        logger.info("BadHeaderError")
    except Exception as e:
        logger.error(e)
    server.quit()
    return "message sent"
