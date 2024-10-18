import os

ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'dev')

if ENVIRONMENT == 'prod':
    from .prod import *
else:
    from .dev import *