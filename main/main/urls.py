from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


### Definice URL patternů pro aplikaci
urlpatterns = [

    # URL pro administrátorské rozhraní Django
    path('admin/', admin.site.urls),

    # URL pro TinyMCE editor
    path('tinymce/', include('tinymce.urls')),


    ### Adresy pro domácí stránku
    # URL's pro domácí stránku
    path('', include('homepage.urls.homepage')),

    # URL pro editaci domácí stránky
    path('edit/', include('homepage.urls.homepage_edit')),


    ### Adresy pro stránky s články
    # Adresy pro stránku s více články
    path('articles/', include('articles.urls.articles')),

    # Adresy pro stránku s jedním článkem
    path('article/', include('articles.urls.article')),

    # Adresy pro vyhledávání v článcích
    path('search/', include('articles.urls.search')),

    # Adresy pro vlastní články
    path('my-articles/', include('articles.urls.my_articles')),


    ### Adresy pro správu uživatelů
    # Adresy pro správu uživatelů
    path('accounts/', include('users.urls.accounts')),

    # Adresy pro správu uživatelského účtu
    path('profile/', include('users.urls.profile')),

    # Adresy pro nastavení postranního panelu
    path('settings/', include('users.urls.sidebar')),

]

# Přidání URL patternů pro statické a média soubory, pokud je nastavený DEBUG mód
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
