### Soubor sloužící k k definování mapování URL adres (Uniform Resource Locators) na pohledy (views) v rámci aplikace ###

# Import modulů:
'''
django.contrib.admin: Tato část obsahuje funkcionality a nástroje pro administraci vaší webové aplikace.
admin: v Django umožňuje snadnou tvorbu administrátorského rozhraní, kde můžete spravovat data uložená v databázi a další administrativní úkony
django.urls: Tento modul poskytuje nástroje pro správu URL adres a routování v aplikaci.
path: znamená, že se z této části používá funkce path, která slouží k definování cest URL a mapování na pohledy.
from django.conf import settings: Tento import načítá modul settings z django.conf, který umožňuje přistupovat k nastavením Django, definovaným ve souboru settings.py
from django.conf.urls.static import static: Tento import načítá funkci static z modulu django.conf.urls.static. Tato funkce je používána k definování URL cesty pro servírování statických souborů (včetně médií) v režimu vývoje.
'''
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.views import index, blog


# Definice URL cest a odpovídajícího mapování na pohledy
'''
'admin/': je cesta mapována na administrační rozhraní Django.
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
]


# Ověření vývojového režimu:
# (Význam této podmínky spočívá ve změně chování aplikace v závislosti na tom, zda je aktivní vývojový režim nebo ne)
# (V praxi to znamená, že při vývoji můžete přistupovat k těmto souborům přímo z webového prohlížeče, aniž byste je museli spravovat přes webserver. Ve výrobním prostředí by mělo být toto chování zakázáno, protože by mohlo představovat bezpečnostní rizika.)
'''
urlpatterns: je seznam obsahující definice URL tras v Django. Tyto trasy určují, jak mají být zpracovávány různé URL požadavky ve vaší aplikaci.
settings.STATIC_URL: obsahuje URL pro statické soubory, například "/static/".
settings.STATIC_ROOT: obsahuje cestu k adresáři, ve kterém jsou statické soubory uloženy na serveru.
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT): přidává cestu pro servírování statických souborů.
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): přidává cestu pro servírování mediálních souborů
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)