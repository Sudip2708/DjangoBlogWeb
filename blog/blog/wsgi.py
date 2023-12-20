### Soubor pro webové servery, které podporují standard WSGI (Web Server Gateway Interface).


import os
from django.core.wsgi import get_wsgi_application
'''
[from]
django.core.wsgi: modul, který obsahuje implementaci WSGI (Web Server Gateway Interface) pro spuštění Django aplikací na webových serverech, které podporují tento standard
[import]
os: modul, který poskytuje přístup k některým funkcím operačního systému
get_wsgi_application: funkce, která vytváří WSGI (Web Server Gateway Interface) aplikaci pro běh Django projektu 
'''


# Nastavení prostředí:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
'''
os: modul, který poskytuje funkce pro interakci s operačním systémem
.environ: slovník, který obsahuje aktuální proměnné prostředí
.setdefault():  metoda slovníku, která nastavuje hodnotu klíče v případě, že klíč ve slovníku ještě není definován
'DJANGO_SETTINGS_MODULE': klíč, který Django používá k určení, který soubor s nastavením má použít
'blog.settings': hodnota, která je nastavena pro klíč 
'''

# Vytvoření WSGI aplikace:
application = get_wsgi_application()
'''
application: označení pro WSGI aplikaci, název proměnné, která drží WSGI aplikaci v konfiguračních skriptech nebo souborech
get_wsgi_application(): funkce, která vytváří WSGI (Web Server Gateway Interface) aplikaci pro běh Django projektu
'''
