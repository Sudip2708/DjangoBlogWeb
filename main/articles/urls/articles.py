from django.urls import path

from ..views.article_list import ArticleListView


# Defining URLs starting with the prefix 'articles/'
urlpatterns = [

    # Display all articles.
    path('all', ArticleListView.as_view(), name='article-list'),

    # Display articles for the selected category.
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='article-category-list'),

    # Display articles for the selected tag.
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag-list'),

    # Display articles for the selected tag, sorted by categories.
    path('tag/<slug:tag_slug>/category/<slug:category_slug>/', ArticleListView.as_view(),
         name='article-tag-list-category'),

    # Display similar articles for the selected tag (based on matching tags).
    path('tag/<slug:tag_slug>/similar/', ArticleListView.as_view(), name='article-tag-list-similar'),

    # Display similar articles for the selected tag, sorted by categories.
    path('tag/<slug:tag_slug>/similar/category/<slug:category_slug>/', ArticleListView.as_view(),
         name='article-tag-list-similar-category'),

]
