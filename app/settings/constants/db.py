from ..utils import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_var("POSTGRES_DB"),
        'USER': get_env_var("POSTGRES_USER"),
        'PASSWORD': get_env_var("POSTGRES_PASSWORD"),
        'HOST': get_env_var("DB_HOST"),
        'PORT': get_env_var("DB_PORT"),
    }
}
