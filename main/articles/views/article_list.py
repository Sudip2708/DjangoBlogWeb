print("### main/articles/views/article_list.py")

### Definice třídy pohledu pro výpis článků

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.urls import resolve

from articles.models.article import Article
from articles.models.article_category import ArticleCategory
from .article_common_contex_mixin import CommonContextMixin
from articles.schema import ArticleSchema


class ArticleListView(CommonContextMixin, ListView):
    # Použitý model pro seznam článků
    model = Article

    # Cesta k šabloně pro zobrazení seznamu článků
    template_name = '3_articles/30__base__.html'

    # Název objektu v kontextu (seznam článků)
    context_object_name = 'queryset'

    # Počet článků na stránku
    paginate_by = 4

    # Název pro aktuální záložku kategorií
    current_category_tab = None


    def get_queryset(self, *args, **kwargs):

        # Získání informací o vyřešené URL z aktuálního požadavku
        resolved_url = resolve(self.request.path_info)
        print("### resolved_url: ",resolved_url)

        # Když jsme na stránce pro zobrazení všech článků
        if resolved_url.route == 'articles/all':
            print("### if route == 'articles/all'")

            self.current_category_tab = 'all'
            print("### current_tab: ", self.current_category_tab)

            status = 'publish'
            article_ids = ArticleSchema().find_all_articles_by_status(status)
            print("### article_ids: ", article_ids)

            queryset = Article.objects.filter(id__in=article_ids).order_by('-created')

        # Když jsme na stránce pro zobrazení článků pro danou kategorii
        elif self.kwargs.get('category_slug'):
            print("### elif self.kwargs.get('category_slug')")

            self.current_category_tab = self.kwargs.get('category_slug')
            print("### current_tab: ", self.current_category_tab)

            category_id = ArticleCategory().get_category_id_by_slug(self.current_category_tab)
            article_ids = ArticleSchema().find_all_articles_by_category(str(category_id))
            print("### article_ids: ", article_ids)

            queryset = Article.objects.filter(id__in=article_ids).order_by('-created')

        # Když jsme na stránce pro zobrazení článků pro výsledek hledání
        # tag_slug = self.kwargs.get('tag_slug')
        # category_slug = self.kwargs.get('category_slug')
        #
        # if self.kwargs.get('current_tab'):
        #     self.current_tab = self.kwargs.get('current_tab')
        #     if self.current_tab == 'all':
        #         queryset = self.current_queryset
        #     elif self.current_tab == 'similar':
        #         queryset = self.current_queryset
        #
        #     else:
        #         print("### current_tab != all")
        #         category = get_object_or_404(ArticleCategory, slug=self.current_tab)
        #         queryset = Article.objects.filter(status='publish', category=category).order_by('-created')
        #
        # elif tag_slug:
        #     # Pokud je k dispozici tag_slug, vyfiltrovat články podle tagu
        #     tag = get_object_or_404(Tag, slug=tag_slug)
        #     queryset = Article.objects.filter(status='publish', tags=tag).order_by('-created')
        #
        # elif category_slug:
        #     # Pokud je k dispozici category_slug, vyfiltrovat články podle kategorie
        #     category = get_object_or_404(ArticleCategory, slug=category_slug)
        #     queryset = Article.objects.filter(status='publish', category=category).order_by('-created')
        #
        # else:
        #     # Jinak vrátit všechny články, seřazené podle data vytvoření
        #     queryset = Article.objects.filter(status='publish').order_by('-created')

        return queryset


    def get_paginate_by(self, queryset):
        print("### def get_paginate_by(self, queryset):")

        # Získání přihlášeného uživatele
        user = self.request.user

        # Pokud je uživatel přihlášený a má pole sidebar nastavené na False, nastavte paginate_by na 6, jinak na 4
        if user.is_authenticated and not user.sidebar:
            return 6
        return 4


    def get_context_data(self, **kwargs):
        print("### def get_context_data(self, **kwargs):")

        # Získání kontextu od rodičovské třídy
        context = super().get_context_data(**kwargs)

        # Získání přihlášeného uživatele
        user = self.request.user

        # Získání kategorií
        if user.is_authenticated and user.sidebar_category_navigation:

            # Přidání množiny kategorií do kontextu
            categories = ArticleCategory.get_all_category_except_default()
            context['categories'] = categories

            # Přidání jména aktuální záložky
            context['current_tab'] = self.current_category_tab

        else:


            # Přidání jména aktuální záložky
            context['current_tab'] = self.current_category_tab

            # Přidání jména aktuální záložky
            category_id = ArticleCategory().get_category_title_by_slug(self.current_category_tab)
            context['current_tab_name'] = category_id


        return context