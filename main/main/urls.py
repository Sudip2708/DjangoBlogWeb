print("### main/main/urls.py")

### Definice URL patternů pro aplikaci

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Adresy začínající s 'admin/'
    # URL pro administrátorské rozhraní Django
    path('admin/', admin.site.urls),

    # Adresy začínající s 'tinymce/'
    # URL pro TinyMCE editor
    path('tinymce/', include('tinymce.urls')),


    ### Adresy pro domácí stránku
    # URL's pro domácí stránku
    path('', include('homepage.urls_homepage')),

    # URL pro editaci domácí stránky
    path('edit/', include('homepage.urls_homepage_edit')),


    ### Adresy pro stránky s články
    # Adresy začínající s 'articles/'
    path('articles/', include('articles.urls_articles')),

    # Adresy začínající s 'article/'
    path('article/', include('articles.urls_article')),

    # Adresy začínající s 'search/'
    path('search/', include('articles.urls_search')),

    # Adresy začínající s 'my-articles/'
    path('my-articles/', include('articles.urls_my_articles')),


    ### Adresy pro správu uživatelů
    # Adresy začínající s 'accounts/'
    path('accounts/', include('users.urls_accounts')),

    # Adresy začínající s 'profile/'
    path('profile/', include('users.urls_profile')),

    # Adresy začínající s 'user_sidebar/'
    path('sidebar/', include('users.urls_sidebar')),


]

# Přidání URL patternů pro statické a média soubory, pokud je nastavený DEBUG mód
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
