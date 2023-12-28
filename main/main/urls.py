### Definice URL patternů pro aplikaci

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from articles.views.home_page import HomePageView
from articles.views.article_create import ArticleCreateView
from articles.views.article_delete import ArticleDeleteView
from articles.views.article_detail import ArticleDetailView
from articles.views.article_list import ArticleListView
from articles.views.article_update import ArticleUpdateView
from articles.views.search import SearchView
from marketing.views import email_list_signup


urlpatterns = [
    # URL pro administrátorské rozhraní Django
    path('admin/', admin.site.urls),

    # URL pro domovskou stránku
    path('', HomePageView.as_view(), name='home'),

    # URL pro seznam článků
    path('articles/', ArticleListView.as_view(), name='article-list'),

    # URL pro vytvoření nového článku
    path('articles/create/', ArticleCreateView.as_view(), name='article-create'),

    # URL pro zobrazení detailu článku s využitím jeho slugu
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),

    # URL pro aktualizaci článku s využitím jeho slugu
    path('articles/<slug:slug>/update/', ArticleUpdateView.as_view(), name='article-update'),

    # URL pro smazání článku s využitím jeho slugu
    path('articles/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

    # URL pro přihlášení k odběru e-mailového seznamu
    path('email-signup/', email_list_signup, name='email-list-signup'),

    # URL pro zobrazení seznamu článků s daným tagem
    path('articles/tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag-list'),

    # URL pro zobrazení seznamu článků v dané kategorii
    path('articles/category/<slug:category_slug>/', ArticleListView.as_view(), name='article-category-list'),

    # URL pro vyhledávání článků
    path('search/', SearchView.as_view(), name='article-search'),

    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('search/<str:query>/', SearchView.as_view(), name='article-search-results'),

    # URL pro TinyMCE editor
    path('tinymce/', include('tinymce.urls')),

    # URL pro účet uživatele (registrace, přihlášení, atd.)
    path('accounts/', include('allauth.urls')),
]

# Přidání URL patternů pro statické a média soubory, pokud je nastavený DEBUG mód
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
