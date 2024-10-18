from .base import *

if os.getenv('simple_app') == 'prod':
   from .prod import *
else:
   from .dev import *