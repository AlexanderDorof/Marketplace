import os
from pathlib import Path

from marketplace import secretkeys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secretkeys.SECRET_KEY

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # pip install:
    "crispy_forms",
    "crispy_bootstrap5",
    "django_filters",
    "rest_framework",
    # apps:
    "main_app",
    "signals",
    "custpanel",
    "crud_db",
    "register",
    "rest_api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "marketplace.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "marketplace.wsgi.application"

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []

# for docker containers and deploing on server (works if DEBUG=False) otherwise static files are not loaded
# STATIC_ROOT = ''
# STATICFILES_DIRS = ['static',]


# Media files: photos

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Form pretiffy with bootstrap 5

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# REDIS consts
REDIS_HOST = "redis"
# REDIS_HOST = 'localhost'
REDIS_PORT = "6379"
REDID_DB = 0

# Celery - prefix with CELERY_
CELERY_BROKER_URL = (
    f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDID_DB}"  # redis://redis:6379/0
)
CELERY_BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TRACK_STARTED = True

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"  # yandex is used as email host
# yandex requires 465 port because it uses SSL (587 port is used for TLS protocol)
EMAIL_PORT = "465"
EMAIL_USE_SSL = True  # add your own settings here

EMAIL_HOST_USER = "aleksandar.dorofeichik@yandex.ru"  # my email address on yandex
EMAIL_HOST_PASSWORD = secretkeys.YANDEX_EMAIL_PASSWORD  # password

# environment variables - without'em django smtp protocol doesn't work
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # my email address
EMAIL_SERVER = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
