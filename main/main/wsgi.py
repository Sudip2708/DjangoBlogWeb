### Soubor pro webové servery, které podporují standard WSGI (Web Server Gateway Interface).

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()
