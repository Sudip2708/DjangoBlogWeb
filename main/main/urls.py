### Definice URL patternů pro aplikaci

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import LoginView, SignupView

from articles.views.home_page import HomePageView
from articles.views.article_create import ArticleCreateView
from articles.views.article_delete import ArticleDeleteView
from articles.views.article_detail import ArticleDetailView
from articles.views.article_list import ArticleListView
from articles.views.article_update import ArticleUpdateView
from articles.views.search import SearchView
from users.views.profile_update_user import profile_update_user
from users.views.profile_update_author import profile_update_author
from users.views.user_sidebar_movements import user_sidebar_movements
from users.views.user_sidebar_appearance import user_sidebar_appearance
from articles.views.my_articles import MyArticlesView

urlpatterns = [
    # URL pro administrátorské rozhraní Django
    path('admin/', admin.site.urls),

    # URL pro domovskou stránku
    path('', HomePageView.as_view(), name='home'),

    # URL pro seznam článků
    path('articles/', ArticleListView.as_view(), name='article-list'),

    # URL pro vytvoření nového článku
    path('articles/create/<str:current_tab>/', ArticleCreateView.as_view(), name='article-create'),

    # URL pro zobrazení detailu článku s využitím jeho slugu
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),

    # URL pro aktualizaci článku s využitím jeho slugu
    path('articles/<slug:slug>/update/<str:current_tab>/', ArticleUpdateView.as_view(), name='article-update'),

    # URL pro smazání článku s využitím jeho slugu
    path('articles/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

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


    # URL pro přihlášení pomocí sociálních sítí
    path('accounts/', include('allauth.socialaccount.urls')),

    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),


    path('profile/update/user', profile_update_user, name='profile_update_user'),
    path('profile/update/author', profile_update_author, name='profile_update_author'),

    # URL pro zobrazení seznamu článků autora
    path('articles/from/<slug:author_slug>/', ArticleListView.as_view(), name='article-from-author-list'),

    # URL pro seznam článků
    path('my-articles/<str:current_tab>/', MyArticlesView.as_view(), name='my-articles'),

    # URL pro aktualizaci stavuotevřených postranních panelů
    path('user_sidebar_appearance/', user_sidebar_appearance, name='user_sidebar_appearance'),
    # URL pro saktualizaci otevřených postranních panelů
    path('user_sidebar_movements/<str:hash>/', user_sidebar_movements, name='user_sidebar_movements'),
]

# Přidání URL patternů pro statické a média soubory, pokud je nastavený DEBUG mód
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
