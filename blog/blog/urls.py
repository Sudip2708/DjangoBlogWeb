### Definuje URL směrovač, který určuje, jak mají být zpracovány příchozí HTTP požadavky


# Import modulů:
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import index, blog, post, search, post_create, post_update, post_delete
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
include: umožňuje zahrnout (importovat) další soubory urls.py do aktuálního souboru urls.py
settings: soubor, který obsahuje nastavení pro konfiguraci Django projektu nebo aplikace
static: modul, který odkazuje na statické soubory, jako jsou obrázky, CSS a JavaScript
index: pohled, který zpracovává požadavky na úvodní stránku
blog: pohled, který se stará o zobrazování seznamu příspěvků
post: pohled, který zpracovává požadavky na zobrazení konkrétního příspěvku
post_create: pohled, který se stará o vytvoření příspěvku
post_update: pohled, který se stará o zobrazování úpravy příspěvku
post_delete: pohled, který se stará o zobrazování smazání příspěvku
'''


# Definice URL cest a odpovídajícího mapování na pohledy
'''
path('admin/', admin.site.urls): adresa a cesta k administrační rozhraní Django
path('', index): adresa a cesta, na úvodní stránku
path('blog/', blog, name='post-list'): adresa, cesta a jméno, na stránku všech příspěvků
path('post/<pk>/', post, name='post-detail'): adresa, cesta a jméno, na stránku konkrétního příspěvku
path('search/', search, name='search'): adresa, cesta a jméno, pro vyhledávání na stránce všech příspěvků
path('tinymce/', include('tinymce.urls')): adresa a cesta, na k zobrazení tinymce (zde zobrazovače a editora článků)
path('post/<id>/update/', post_update, name='post-update'): adresa, cesta a jméno, pro úpravu příspěvku
path('post/<id>/delete/', post_delete, name='post-delete'): adresa, cesta a jméno, pro smazání příspěvku
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<pk>/', post, name='post-detail'),
    path('search/', search, name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('create/', post_create, name='post-create'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
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