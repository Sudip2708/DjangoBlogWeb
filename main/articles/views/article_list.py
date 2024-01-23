### Definice třídy pohledu pro výpis článků

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from articles.models.article import Article, ArticleCategory
from utilities.for_articles.views_common_contex_mixin import CommonContextMixin


class ArticleListView(CommonContextMixin, ListView):
    # Použitý model pro seznam článků
    model = Article

    # Cesta k šabloně pro zobrazení seznamu článků
    template_name = '30_articles.html'

    # Název objektu v kontextu (seznam článků)
    context_object_name = 'queryset'

    # Počet článků na stránku
    paginate_by = 4

    def get_queryset(self):
        # Získání hodnot slugů z URL pro filtrování článků
        tag_slug = self.kwargs.get('tag_slug')
        category_slug = self.kwargs.get('category_slug')

        if tag_slug:
            # Pokud je k dispozici tag_slug, vyfiltrovat články podle tagu
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = Article.objects.filter(tags=tag).order_by('-created')
        elif category_slug:
            # Pokud je k dispozici category_slug, vyfiltrovat články podle kategorie
            category = get_object_or_404(ArticleCategory, slug=category_slug)
            queryset = Article.objects.filter(categories=category).order_by('-created')
        else:
            # Jinak vrátit všechny články, seřazené podle data vytvoření
            queryset = Article.objects.order_by('-created')

        return queryset

