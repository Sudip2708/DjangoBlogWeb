print("### main/articles/views/article_list.py")

### Definice třídy pohledu pro výpis článků

from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.urls import resolve

from articles.models.article import Article
from .article_common_contex_mixin import CommonContextMixin
from articles.schema_methods.find_all_articles_by_status import find_all_articles_by_status
from articles.schema_methods.find_published_articles_by_tag import find_published_articles_by_tag
from articles.schema_search.get_article_ids_for_similar_articles import get_article_ids_for_similar_articles
from articles.schema_search.get_category_articles_ids import get_category_articles_ids
from articles.schema_search.get_all_published_category import get_all_published_category


class ArticleListView(CommonContextMixin, ListView):
    '''
    Pohled pro zobrazení seznamu článků

    Pohled obsahuje logiku pro načítání dat z databáze a jejich zobrazení ve správném formátu.
    Využívá model Article pro přístup k datům a definuje cestu k šabloně pro zobrazení.
    Navíc obsahuje metodu get_queryset, která filtruje články na základě aktuálního kontextu stránky,
    jako jsou kategorie nebo tagy.
    Metoda get_paginate_by slouží k nastavení počtu článků na stránce v závislosti na tom,
    zda je uživatel přihlášený a má zapnutý boční panel.
    Nakonec metoda get_context_data přidává další informace do kontextu pro šablonu,
    jako jsou aktuálně vybraná kategorie nebo tag
    '''

    # Použitý model pro seznam článků
    model = Article

    # Cesta k šabloně pro zobrazení seznamu článků
    template_name = '3_articles/30__base__.html'

    ## Název objektu pro výsledný seznam článků
    context_object_name = 'articles_results'

    # Jméno adresy URL
    url_name = ""

    # Aktuálně přihlášený uživatel
    user = None

    # Výsledný seznam ID článků
    article_ids = []

    # Ověření zda má uživatel pro daný pohled zapnutou i navigaci
    navigation = False

    # Slovník hodnot pro aktuální kategorii (nastaveno na první přepnutí na kategorie)
    current_category_tab = {'id': 0, 'slug': 'first', 'title': ''}

    # Slovník hodnot pro kategorie pro vytvoření záložek navigace
    category_items = {}

    # Slovník hodnot pro aktuální tag
    current_tag_tab = {}


    def get_queryset(self, *args, **kwargs):
        '''
        Metoda slouží k získání souboru článků, které mají být zobrazeny na stránce na základě aktuálního požadavku.

        Tato metoda slouží k vyhledání a filtrování článků na základě aktuálního kontextu stránky.
        Nejprve analyzuje aktuální URL adresu, aby určila, zda se jedná o seznam všech článků,
        seznam článků v kategorii nebo seznam článků pro konkrétní tag.
        Poté na základě těchto informací získá relevantní články z databáze.
        Pokud je uživatel přihlášen a má zapnutou navigaci podle kategorií,
        metoda získává také informace o dostupných kategoriích.

        :param args: Pozicí argumenty, které mohou být předány metodě.
        :param kwargs: Klíčové argumenty, které mohou být předány metodě.
        :return: Queryset obsahující relevantní články, které jsou následně zobrazeny na stránce.
        '''

        # Kontrolní tisk všech atributu z cesty:
        # resolved_url = resolve(request.path_info)
        # print("### resolved_url: ", resolved_url)

        # Přiřazení jména URL adresy
        self.url_name = resolve(self.request.path_info).url_name

        # Získání přihlášeného uživatele
        self.user = self.request.user

        # Ověření, zda se jedná o stránku se všemi články a nebo o stránky s kategoriemi
        if self.url_name == 'article-list' or self.url_name == 'article-category-list':

            # Ověření zda uživatel má zaplé zobrazení navigace kategorií
            if self.user.sidebar_category_navigation:
                self.navigation = True

            # Vyhledání ID článků v schematu pro všechny publikované články
            self.article_ids = find_all_articles_by_status('publish')

            # Pokud jsme na hlavní stránce pro všechny články
            if self.url_name == 'article-list':

                # Nastavení záložky pro stránku se všemi články
                self.current_category_tab = {'id': 0, 'slug': 'all', 'title': 'All'}

                # Ověření, zda má uživatel zapnuté kategorie a získání všech kategoriích
                if self.navigation:
                    self.category_items = get_all_published_category()

        # Když jsme na stránce pro zobrazení článků pro daný tag
        elif self.kwargs.get('tag_slug'):

            # Ověření zda uživatel má zaplé zobrazení navigace kategorií
            if self.user.show_tab_for_similar:
                self.navigation = True

            # Vyhledání tagu a přiřazení do atributu
            tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
            self.current_tag_tab = {'id': tag.id, 'slug': tag.slug, 'title': tag.name}

            # Získání ID článků pro zadaný tag
            self.article_ids = find_published_articles_by_tag(str(tag.id))

            # Získání ID článků pro podobné články pro zadaný tag
            if 'similar' in self.url_name:
                self.article_ids = get_article_ids_for_similar_articles(self.article_ids)

        # Získání kategorií pro zobrazení stránky s kategoriema
        if 'category' in self.url_name:

            # Vytažení aktuální záložky z URL adresy
            current_category_tab_slug = self.kwargs['category_slug']

            # Získání ID článků a aktuální kategorie a seznamu kategorií dle zadaných parametrů
            ids, tab, cat = get_category_articles_ids(self.article_ids, current_category_tab_slug)
            self.article_ids = ids
            self.current_category_tab = tab
            self.category_items = cat

        # Získání a navrácení článků z databáze dle ID nalezených ve schématu
        queryset = Article.objects.filter(id__in=self.article_ids).order_by('-created')
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

        # Pokud uživatel má zobrazen postranní panel, stránkuj po 4, jinak po 6
        if self.user.sidebar:
            return 4
        return 6


    def get_context_data(self, **kwargs):
        '''
        Metoda pro vytvoření kontextu pro šablonu.

        Tato metoda vytváří kontext pro šablonu, který obsahuje data, která jsou použita k vykreslení stránky.
        Nejprve získá běžný kontext voláním nadřazené metody `super().get_context_data(**kwargs)`.
        Poté přidává další informace do kontextu jako je jméno URL, ověření zobrazení navigace,
        aktuálně vybraná kategorie a tag (pokud je relevantní), seznam zobrazených kategorií a další.

        :param kwargs: Klíčové argumenty, které mohou být předány metodě.
        :return: Kontext s vloženými daty pro šablonu.
        '''

        # Získání kontextu od rodičovské třídy
        context = super().get_context_data(**kwargs)

        # Přidání jména URL
        context['url_name'] = self.url_name

        # Přidání ověření, zda má být zobrazena navigace
        context['navigation'] = self.navigation

        # Přidání aktuálně vybranou kategorii
        context['current_category_tab'] = self.current_category_tab

        # Pokud jsme na stránce s podobnýmy články na základě tagu
        if self.kwargs.get('tag_slug'):

            # Přidání aktuálně vybraný tag
            context['current_tag_tab'] = self.current_tag_tab

        # Pokud je zapnuté navigace pro podobné články
        if self.navigation:

            # Přidání seznamu zobrazených kategorií
            context['category_items'] = self.category_items

        # Navrácení kontextu
        return context