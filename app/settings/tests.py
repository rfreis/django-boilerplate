from .base import *

default_db_name = DATABASES['default']['NAME']
DATABASES['default']['NAME'] = f'test_{default_db_name}'
