from django.urls import path

from ..views.article_list import ArticleListView


# Definování adres začínajících s prefixem 'articles/'
urlpatterns = [

    # Zobrazení všech článků.
    path('all', ArticleListView.as_view(), name='article-list'),

    # Zobrazení článků pro vybranou kategorii.
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='article-category-list'),

    # Zobrazení článků pro vybraný tag.
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag-list'),

    # Zobrazení článků pro vybraný tag, rostříděných dle kategorií.
    path('tag/<slug:tag_slug>/category/<slug:category_slug>/', ArticleListView.as_view(),
         name='article-tag-list-category'),

    # Zobrazení podobných článků pro vybraný tag (na základě shodných tagů).
    path('tag/<slug:tag_slug>/similar/', ArticleListView.as_view(), name='article-tag-list-similar'),

    # Zobrazení podobných článků pro vybraný tag, rostříděných dle kategorií.
    path('tag/<slug:tag_slug>/similar/category/<slug:category_slug>/', ArticleListView.as_view(),
         name='article-tag-list-similar-category'),

]












