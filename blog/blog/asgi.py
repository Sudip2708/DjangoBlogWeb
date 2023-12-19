### Soubor pro asynchronní webové servery, které podporují standard ASGI (Asynchronous Server Gateway Interface).


import os
from django.core.asgi import get_asgi_application
'''
os: modul, který poskytuje přístup k některým funkcím operačního systému
django.core.asgi: balíček, který obsahuje nástroje pro vytváření aplikací s asynchronním obsluhováním (ASGI - Asynchronous Server Gateway Interface)
get_asgi_application: funkce, která slouží k získání asynchronní aplikace pro obsluhu požadavků pomocí ASGI 
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
application = get_asgi_application()
'''
application: označení pro WSGI aplikaci, název proměnné, která drží WSGI aplikaci v konfiguračních skriptech nebo souborech
get_asgi_application(): funkce, která  slouží k získání instance asynchronní aplikace pro obsluhu požadavků pomocí ASGI (Asynchronous Server Gateway Interface)
'''
