### Definice třídy pohledu pro výpis článků

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from articles.models.article import Article, ArticleCategory
from .article_common_contex_mixin import CommonContextMixin
from articles.models.article_author import ArticleAuthor


class MyArticlesView(CommonContextMixin, ListView):
    # Použitý model pro seznam článků
    model = Article

    # Cesta k šabloně pro zobrazení seznamu článků
    template_name = '3_articles/30__base__.html'

    # Název objektu v kontextu (seznam článků)
    context_object_name = 'queryset'

    # Počet článků na stránku
    paginate_by = 4

    # Název stránky
    page_title = "My Articles"

    def get_context_data(self, **kwargs):
        # Získání kontextu od rodičovské třídy
        context = super().get_context_data(**kwargs)
        # Přidání názvu stránky do kontextu
        context['page_title'] = self.page_title
        # Přidání aktuální záložky do kontextu
        context['current_tab'] = self.kwargs.get('current_tab')
        return context

    def get_queryset(self):
        # Získání hodnot slugů z URL pro filtrování článků
        tag_slug = self.kwargs.get('tag_slug')
        category_slug = self.kwargs.get('category_slug')
        current_tab = self.kwargs.get('current_tab')

        if tag_slug:
            # Pokud je k dispozici tag_slug, vyfiltrovat články podle tagu
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = Article.objects.filter(tags=tag).order_by('-created')
        elif category_slug:
            # Pokud je k dispozici category_slug, vyfiltrovat články podle kategorie
            category = get_object_or_404(ArticleCategory, slug=category_slug)
            queryset = Article.objects.filter(category=category).order_by('-created')
        else:
            # Pokud je k dispozici current_tab, filtrovat články podle vybrané záložky
            user = self.request.user
            author = ArticleAuthor.objects.get(id=user.linked_author_id)
            if current_tab == 'drafted':
                queryset = Article.objects.filter(author=author, status='drafted').order_by('-created')
            elif current_tab == 'publish':
                queryset = Article.objects.filter(author=author, status='publish').order_by('-created')
            elif current_tab == 'archive':
                queryset = Article.objects.filter(author=author, status='archive').order_by('-created')
            else:
                queryset = Article.objects.filter(author=author).order_by('-created')

        return queryset

