### Definuje URL směrovač, který určuje, jak mají být zpracovány příchozí HTTP požadavky


# Import modulů:
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posts.views import index, blog, post
'''
[from]
django.contrib: balíček, který obsahuje moduly a aplikace poskytující dodatečnou funkcionalitu.
django.urls: balíček, který obsahuje funkce a třídy pro práci s URL v aplikaci
django.conf: balíček, který obsahuje nastavení pro konfiguraci Django aplikace
django.conf.urls.static: balíček, který obsahuje funkce související s obsluhou statických souborů, jako jsou obrázky, CSS a JavaScript
posts.views: soubor views.py ve složce posts, které definuje pohledy obsluhují HTTP požadavky
[import]
admin: modul, který odkazuje na administrátorské rozhraní Django, které je poskytováno modulem django.contrib.admin
path: třída, která se používá k definici URL cest ve views
settings: soubor, který obsahuje nastavení pro konfiguraci Django projektu nebo aplikace
static: modul, který odkazuje na statické soubory, jako jsou obrázky, CSS a JavaScript
index: pohled, který zpracovává požadavky na úvodní stránku
blog: pohled, který se stará o zobrazování seznamu příspěvků
post: pohled, který zpracovává požadavky na zobrazení konkrétního příspěvku
'''


# Definice URL cest a odpovídajícího mapování na pohledy
'''
path('admin/', admin.site.urls): adresa a cesta, mapována na administrační rozhraní Django
path('', index): adresa a cesta, mapována na úvodní stránku
path('blog/', blog): adresa a cesta, mapována na zobrazování seznamu příspěvků
path('post/', post): adresa a cesta, mapována na zobrazení konkrétního příspěvku
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
]


# Ověření vývojového režimu:
# (Význam této podmínky spočívá ve změně chování aplikace v závislosti na tom, zda je aktivní vývojový režim nebo ne)
# (V praxi to znamená, že při vývoji můžete přistupovat k těmto souborům přímo z webového prohlížeče, aniž byste je museli spravovat přes webserver. Ve výrobním prostředí by mělo být toto chování zakázáno, protože by mohlo představovat bezpečnostní rizika.)
'''
urlpatterns: seznam obsahující definice URL tras v Django. Tyto trasy určují, jak mají být zpracovávány různé URL požadavky ve vaší aplikaci.
settings.STATIC_URL: obsahuje URL pro statické soubory, například "/static/".
settings.STATIC_ROOT: obsahuje cestu k adresáři, ve kterém jsou statické soubory uloženy na serveru.
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT): přidává cestu pro servírování statických souborů.
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): přidává cestu pro servírování mediálních souborů
'''
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)