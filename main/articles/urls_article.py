print("### main/main/urls.py")

from django.urls import path

# Pohledy pro článek
from articles.views.article_create import ArticleCreateView
from articles.views.article_delete import ArticleDeleteView
from articles.views.article_detail import ArticleDetailView
from articles.views.article_update import ArticleUpdateView


urlpatterns = [

    # Adresy začínající s 'article/'
    # URL pro vytvoření nového článku
    path('create/<str:current_tab>/', ArticleCreateView.as_view(), name='article-create'),
    # URL pro zobrazení detailu článku s využitím jeho slugu
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    # URL pro aktualizaci článku s využitím jeho slugu
    path('<slug:slug>/update/<str:current_tab>/', ArticleUpdateView.as_view(), name='article-update'),
    # URL pro smazání článku s využitím jeho slugu
    path('<slug:slug>/delete/', ArticleDeleteView.as_view(), name='article-delete'),

]











