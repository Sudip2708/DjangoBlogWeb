print("### main/main/urls.py")

from django.urls import path

# Pohledy pro články
from articles.views.article_list import ArticleListView


urlpatterns = [

    # Adresy začínající s 'articles/'
    # URL pro seznam článků
    path('all', ArticleListView.as_view(), name='article-list'),
    # URL pro zobrazení seznamu článků v dané kategorii
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='article-category-list'),
    # URL pro zobrazení seznamu článků s daným tagem
    path('tag/<slug:tag_slug>/', ArticleListView.as_view(), name='article-tag-list'),
    # URL pro zobrazení seznamu článků s daným tagem a navigací pro kategorie
    path('tag/<slug:tag_slug>/<str:category>/<slug:category_slug>/', ArticleListView.as_view(), name='article-tag-list-category'),
    # URL pro zobrazení článků se stejnými tagy jako mají články pro daný tag
    path('tag/<slug:tag_slug>/<str:similar>/', ArticleListView.as_view(), name='article-tag-list-similar'),
    # URL pro zobrazení článků se stejnými tagy jako mají články pro daný tag a navigací pro kategorie
    path('tag/<slug:tag_slug>/<str:similar>/<str:category>/<slug:category_slug>/', ArticleListView.as_view(), name='article-tag-list-similar-category'),
    # URL pro zobrazení seznamu článků od určitého autora
    path('from/<slug:author_slug>/', ArticleListView.as_view(), name='article-from-author-list'),

]












