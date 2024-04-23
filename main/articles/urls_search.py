print("### main/main/urls.py")

from django.urls import path

from articles.views.search import SearchView

urlpatterns = [

    # Adresy začínající s 'search/'
    # URL pro vyhledávání článků
    path('search/', SearchView.as_view(), name='article-search'),
    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('search/<str:query>/', SearchView.as_view(), name='article-search-results'),
    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('search/<str:query>/<str:category>/<slug:category_slug>/', SearchView.as_view(), name='article-search-results-category'),
    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('search/<str:query>/<str:similar>/', SearchView.as_view(), name='article-search-similar'),
    # URL pro zobrazení výsledků vyhledávání s daným dotazem
    path('search/<str:query>/<str:similar>/<str:category>/<slug:category_slug>/', SearchView.as_view(), name='article-search-similar-category'),

]









