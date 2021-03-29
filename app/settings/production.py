from .base import *

# Static files & Media

STATIC_ROOT = os.path.join(BASE_DIR, "assets")

STATIC_URL = '/assets/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'

# Logging
from .constants.logging import *
