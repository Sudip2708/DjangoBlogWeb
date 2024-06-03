from django.urls import path

from ..views.article_create import ArticleCreateView
from ..views.article_delete import ArticleDeleteView
from ..views.article_detail import ArticleDetailView
from ..views.article_update import ArticleUpdateView


# Definování adres začínajících s prefixem 'article/'
urlpatterns = [

    # Zobrazení stránky pro vytvoření nového článku.
    path('create/<str:current_tab>/', ArticleCreateView.as_view(), name='article-create'),

    # Zobrazení stránky pro úpravu již existujícího článku.
    path('<slug:slug>/update/<str:current_tab>/', ArticleUpdateView.as_view(), name='article-update'),

    # Stránka pro potvrzení smazání článku.
    path('<slug:slug>/delete/',  ArticleDeleteView.as_view(), name='article-delete'),

    # Zobrazení konkrétního článku.
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),

]











