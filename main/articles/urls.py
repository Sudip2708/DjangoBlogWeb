print("### main/main/urls.py")

### Definice URL patternů pro aplikaci

from django.urls import path

from .views.article_create import ArticleCreateView
from .views.article_delete import ArticleDeleteView
from .views.article_detail import ArticleDetailView
from .views.article_list import ArticleListView
from .views.article_update import ArticleUpdateView
from .views.search import SearchView

urlpatterns = [

    # Adresy začínající s 'articles/'
    # URL pro seznam článků
    path('all', ArticleListView.as_view(), name='article-list'),

    # URL pro zobrazení seznamu článků v dané kategorii
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='article-category-list'),

    # URL pro zobrazení seznamu článků s daným tagem
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag-list'),

    # URL pro zobrazení seznamu článků s daným tagem a navigací pro kategorie
    path('tag/<slug:tag_slug>/<str:category>/<slug:category_slug>/', ArticleListView.as_view(),
         name='article-tag-list-category'),

    # URL pro zobrazení článků se stejnými tagy jako mají články pro daný tag
    path('tag/<slug:tag_slug>/<str:similar>/', ArticleListView.as_view(), name='article-tag-list-similar'),

    # URL pro zobrazení článků se stejnými tagy jako mají články pro daný tag a navigací pro kategorie
    path('tag/<slug:tag_slug>/<str:similar>/<str:category>/<slug:category_slug>/', ArticleListView.as_view(),
         name='article-tag-list-similar-category'),

    # URL pro zobrazení seznamu článků od určitého autora
    path('from/<slug:author_slug>/', ArticleListView.as_view(), name='article-from-author-list'),



    # Adresy začínající s 'article/'
    # URL pro vytvoření nového článku
    path('create/<str:current_tab>/', ArticleCreateView.as_view(), name='article-create'),

    # URL pro zobrazení detailu článku s využitím jeho slugu
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),

    # URL pro aktualizaci článku s využitím jeho slugu
    path('<slug:slug>/update/<str:current_tab>/', ArticleUpdateView.as_view(), name='article-update'),

    # URL pro smazání článku s využitím jeho slugu
    path('<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),


    # Adresy začínající s 'search/'
    # URL pro vyhledávání článků
    path('', SearchView.as_view(), name='article-search'),

    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('<str:query>/', SearchView.as_view(), name='article-search-results'),

    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('<str:query>/<str:category>/<slug:category_slug>/', SearchView.as_view(),
         name='article-search-results-category'),

    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('<str:query>/<str:similar>/', SearchView.as_view(), name='article-search-similar'),

    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('<str:query>/<str:similar>/<str:category>/<slug:category_slug>/', SearchView.as_view(),
         name='article-search-similar-category'),


]

