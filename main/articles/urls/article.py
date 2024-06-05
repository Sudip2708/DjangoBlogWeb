from django.urls import path

from ..views.article_create import ArticleCreateView
from ..views.article_delete import ArticleDeleteView
from ..views.article_detail import ArticleDetailView
from ..views.article_update import ArticleUpdateView


# Defining URLs starting with the prefix 'article/'
urlpatterns = [

    # Display the page for creating a new article.
    path('create/<str:current_tab>/', ArticleCreateView.as_view(), name='article-create'),

    # Display the page for updating an existing article.
    path('<slug:slug>/update/<str:current_tab>/', ArticleUpdateView.as_view(), name='article-update'),

    # Page for confirming the deletion of an article.
    path('<slug:slug>/delete/',  ArticleDeleteView.as_view(), name='article-delete'),

    # Display a specific article.
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),

]
