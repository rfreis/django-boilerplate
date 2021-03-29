import os

from django.core.exceptions import ImproperlyConfigured


def get_env_var(setting, default=None):
    try:
        val = os.environ.get(setting, default)
        if val == 'True':
            val = True
        elif val == 'False':
            val = False
        return val
    except KeyError:
        error_msg = "ImproperlyConfigured: Set environment variable {}".format(setting)
        raise ImproperlyConfigured(error_msg)
