print("### main/articles/views/my_articles.py")

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
    context_object_name = 'articles_results'

    # Název stránky
    page_title = "My Articles"

    def get_queryset(self):

        # Získání hodnot slugů z URL pro filtrování článků
        tag_slug = self.kwargs.get('tag_slug')
        category_slug = self.kwargs.get('category_slug')
        current_tab = self.kwargs.get('current_tab')

        # Pokud je k dispozici tag_slug, vyfiltrovat články podle tagu
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = Article.objects.filter(tags=tag).order_by('-created')

        # Pokud je k dispozici category_slug, vyfiltrovat články podle kategorie
        elif category_slug:
            category = get_object_or_404(ArticleCategory, slug=category_slug)
            queryset = Article.objects.filter(category=category).order_by('-created')

        # Pokud je k dispozici current_tab, filtrovat články podle vybrané záložky
        else:
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



    def get_paginate_by(self, queryset):
        '''
        Metoda pro určení počtu článků na stránce při stránkování výsledků vyhledávání.

        Tato metoda získává přihlášeného uživatele a na základě toho, zda má postranní panel,
        určuje počet článků na stránce. Pokud je uživatel přihlášený a nemá zobrazen postranní panel,
        vrátí hodnotu 6, jinak vrátí hodnotu 4.

        :param queryset: Queryset obsahující výsledky vyhledávání.
        :return: Počet článků na stránce pro stránkování.
        '''

        user = self.request.user
        # Pokud je uživatel přihlášený a nemá zobrazen postranní panel, stránkuj po 6, jinak po 4
        if user.is_authenticated and not user.sidebar:
            return 6
        return 4

    def get_context_data(self, **kwargs):

        # Získání kontextu od rodičovské třídy
        context = super().get_context_data(**kwargs)

        # Přidání názvu stránky do kontextu
        context['page_title'] = 'My Articles'

        # Přidání aktuální záložky do kontextu
        context['current_tab'] = self.kwargs.get('current_tab')

        # Definování jména URL cesty
        context['url_name'] = 'my-articles'

        return context
