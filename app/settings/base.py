from pathlib import Path

from .utils import *


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = get_env_var("SECRET_KEY")

DEBUG = get_env_var("DEBUG")

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

from .constants.local_apps import LOCAL_APPS
from .constants.third_party_apps import THIRD_PARTY_APPS
INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.AuthJWT',
]

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


from .constants.auth import AUTH_PASSWORD_VALIDATORS
from .constants.db import DATABASES
from .constants.drf import REST_FRAMEWORK
from .constants.templates import TEMPLATES
from .constants.jwt import SIMPLE_JWT


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
