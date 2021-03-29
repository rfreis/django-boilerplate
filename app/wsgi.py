import os

from django.core.wsgi import get_wsgi_application

from app.settings.utils import *

SETTINGS_MODULE_PATH = get_env_var('SETTINGS_MODULE_PATH')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE_PATH)

application = get_wsgi_application()
