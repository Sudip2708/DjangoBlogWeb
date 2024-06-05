from django.urls import path

from ..views.search import SearchView
from ..views.search_input import SearchInputView


# Defining URLs starting with the prefix 'search/'
urlpatterns = [

    # Display page for entering search queries for articles.
    path('', SearchView.as_view(), name='article-search'),

    # Display error message for invalid search input.
    path('error/', SearchInputView.as_view(), name='article-search-error'),

    # Page for entering search queries.
    path('input/', SearchInputView.as_view(), name='article-search-input'),

    # Display search results.
    path('<str:query>/', SearchView.as_view(), name='article-search-results'),

    # Display search results sorted by categories.
    path('<str:query>/category/<slug:category_slug>/', SearchView.as_view(),
         name='article-search-results-category'),

    # Display similar articles for the search result (based on matching tags).
    path('<str:query>/similar/', SearchView.as_view(), name='article-search-similar'),

    # Display similar articles for the search result sorted by categories.
    path('<str:query>/similar/category/<slug:category_slug>/', SearchView.as_view(),
         name='article-search-similar-category'),

]
