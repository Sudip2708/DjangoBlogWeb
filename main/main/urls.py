print("### main/main/urls.py")

### Definice URL patternů pro aplikaci

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # URL pro administrátorské rozhraní Django
    path('admin/', admin.site.urls),

    # URL pro TinyMCE editor
    path('tinymce/', include('tinymce.urls')),



    # URL's pro domácí stránku > přesměrování na urls aplikace homepage
    path('', include('homepage.urls')),



    # URL's pro správu přihlášení > přesměrování na urls aplikace users
    path('accounts/', include('users.urls')),

    # URL's pro správu účtů > přesměrování na urls aplikace users
    path('profile/', include('users.urls')),

    # URL's pro správu postranního panelu > přesměrování na urls aplikace users
    path('user_sidebar/', include('users.urls')),



    # URL's pro správu stránek s více články > přesměrování na urls aplikace articles
    path('articles/', include('articles.urls')),

    # URL's pro správu určitého článku > přesměrování na urls aplikace articles
    path('article/', include('articles.urls')),

    # URL's pro hledání v článcích > přesměrování na urls aplikace articles
    path('search/', include('articles.urls')),

]

# Přidání URL patternů pro statické a média soubory, pokud je nastavený DEBUG mód
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












