from django.urls import path

from ..views.search import SearchView
from ..views.search_input import SearchInputView


# Definování adres začínajících s prefixem 'search/'
urlpatterns = [

    # Zobrazení stránky pro zadání dotazu pro vyhledávání v článcích.
    path('', SearchView.as_view(), name='article-search'),

    # Zobrazení oznamu o chybném zadání.
    path('error/', SearchInputView.as_view(), name='article-search-error'),

    # Stránka pro zadání vyhledávání.
    path('input/', SearchInputView.as_view(), name='article-search-input'),

    # Zobrazení výsledků vyhledávání.
    path('<str:query>/', SearchView.as_view(), name='article-search-results'),

    # Zobrazení výsledků vyhledávání, tříděného dle kategorií.
    path('<str:query>/category/<slug:category_slug>/', SearchView.as_view(),
         name='article-search-results-category'),

    # Zobrazení podobných článků pro výsledek vyhledávání (na základě shodných tagů).
    path('<str:query>/similar/', SearchView.as_view(), name='article-search-similar'),

    # Zobrazení podobných článků pro výsledek vyhledávání, tříděného dle kategorií.
    path('<str:query>/similar/category/<slug:category_slug>/', SearchView.as_view(),
         name='article-search-similar-category'),

]









