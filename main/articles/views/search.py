print("### main/articles/views/search.py")

### Definice třídy pohledu pro vyhledávání

from django.views.generic import ListView
from django.shortcuts import redirect
from django.urls import resolve
from django.urls import reverse
import ast

from articles.models.article import Article
from .article_common_contex_mixin import CommonContextMixin
from articles.schema_search.get_article_ids_by_search_params import get_article_ids_by_search_params
from articles.schema_search.get_category_articles_ids import get_category_articles_ids
from articles.schema_search.get_article_ids_for_similar_articles import get_article_ids_for_similar_articles



class SearchView(CommonContextMixin, ListView):
    '''
    Pohled pohled, který zpracovává dotazy pro vyhledávání článků

    Tento pohled umožňuje uživatelům zadat různé parametry pro hledání, jako je klíčové slovo, datum, autor atd.
    Pokud jsou zadány platné parametry, pohled vrátí seznam článků odpovídajících hledání.
    Pokud nejsou zadány žádné parametry, vrátí prázdný seznam.
    Pohled obsahuje metodu get, která zpracovává data zaslaná z vyhledávacího pole a předává je dál na vyřízení.
    Dále obsahuje metodu get_queryset, která získává a filtrová data z databáze na základě zadaných parametrů hledání.
    Metoda get_context_data pak přidává další informace do kontextu pro šablonu,
    jako je jméno URL, dotaz, popis výsledku vyhledávání
    a seznam zobrazených kategorií, pokud je zapnutá navigace pro podobné články.
    '''

    # Použitý model pro seznam článků
    model = Article

    # Cesta k šabloně pro zobrazení seznamu článků
    template_name = '3_articles/30__base__.html'

    # Název objektu pro výsledný seznam článků
    context_object_name = 'articles_results'

    # Jméno adresy URL
    url_name = ""

    # Aktuálně přihlášený uživatel
    user = None

    # Výsledný seznam ID článků
    article_ids = []

    # Výsledný popisný text
    display_text = ""

    # Slovník hodnot pro aktuální kategorii (nastaveno na první přepnutí na kategorie)
    current_category_tab = {'id': 0, 'slug': 'first', 'title': ''}

    # Slovník hodnot pro kategorie pro vytvoření záložek navigace
    category_items = {}

    # Atribut pro záznam prázdného dotazu
    empty_query = False


    def get(self, request, *args, **kwargs):
        '''
        Metoda pro zpracování dotazu pro vyhledávání v článcích.

        Při prvním průchodu metoda předspracuje data a při druhém data předá dál na vyhledávání

        :param request: Objekt HttpRequest, obsahující informace o HTTP požadavku.
        :param args: Pozicí argumenty, které mohou být předány metodě.
        :param kwargs: Klíčové argumenty, které mohou být předány metodě.
        :return: HTTP odpověď s přesměrováním na výsledky vyhledávání nebo výsledek z předchozího volání nadřazené metody.
        '''

        # Kontrolní tisk všech atributu z cesty:
        # resolved_url = resolve(request.path_info)
        # print("### resolved_url: ", resolved_url)

        # Přiřazení jména URL adresy
        self.url_name = resolve(request.path_info).url_name

        # Získání přihlášeného uživatele
        self.user = self.request.user

        # Ověření, zda se jedná o data zaslaná z vyhledávacího pole
        if self.url_name == 'article-search':

            # Vytažení dat z dotazu a vytvoření slovníku pro parametry hledání
            search_parameters = {
                'query': self.request.GET.get('q', ''),
                'title': self.request.GET.get('title_checkbox', ''),
                'overview': self.request.GET.get('overview_checkbox', ''),
                'content': self.request.GET.get('content_checkbox', ''),
                'before': self.request.GET.get('before_date', ''),
                'after': self.request.GET.get('after_date', ''),
                'author': self.request.GET.get('author_select', '')
            }

            # Přeposlání zpracovaného dotazu na vyřízení
            if any(value for value in search_parameters.values()):
                return redirect(reverse('article-search-results', kwargs={'query': search_parameters}))

        # Pokud se již jedná o před-zpracovaný dotaz, bude posunut dál
        else:
            return super().get(request, *args, **kwargs)


    def get_queryset(self):
        '''
        Metoda slouží k získání a filtrování dat z databáze na základě zadaných parametrů hledání.

        Metoda get_queryset(self) zpracovává požadavky na vyhledávání článků na základě zadaných parametrů.
        Nejprve získává parametry hledání a poté na jejich základě vyhledává odpovídající články v databázi.
        Pokud jsou zadány platné parametry, metoda vrátí seznam článků odpovídajících hledání.
        Pokud nejsou zadány žádné parametry, vrátí prázdný seznam.

        :return: Queryset, který obsahuje všechny relevantní články
        '''

        # Pokud nebyly zadány žádné parametry hledání, vrátit prázdný queryset
        # Toto je zde proto, aby načítání postranních panelů nevyvolalo při načítání scriptu
        # pro zprávu vyklápěcí nabídky postranních panelů ValueError
        if not self.request.GET:
            return Article.objects.none()

        # Získání parametrů pro hledání
        search_parameters = ast.literal_eval(self.kwargs.get('query'))

        # Seznam klíčů k ověření
        check_list = ['query', 'before', 'after', 'author']

        # Kontrola, zda je alespoň jedna položka vyplněná
        if any(search_parameters[key] for key in check_list):

            # Získání ID článků a popisného textu dle zadaných parametrů
            self.article_ids, self.display_text = get_article_ids_by_search_params(search_parameters)

            # Získání výsledku pro stránku s podobnými článkami důle tagů
            if self.kwargs.get('similar'):

                # Získání ID článků a popisného textu dle zadaných parametrů
                self.article_ids = get_article_ids_for_similar_articles(self.article_ids)

            # Získání kategorií
            if self.kwargs.get('category'):

                # Vytažení aktuální záložky z URL adresy
                current_category_tab_slug = self.kwargs['category_slug']

                # Ověření, zda je vyfiltrovaný alespoň jeden článek
                if self.article_ids:

                    # Získání ID článků a aktuální kategorie dle zadaných parametrů
                    ids, tab, cat = get_category_articles_ids(self.article_ids, current_category_tab_slug)
                    self.article_ids = ids
                    self.current_category_tab = tab
                    self.category_items = cat

                # Pokud není vyfiltrovaný žádná článek navrácení False
                else:
                    self.category_items = False

        # Pokud nebyl zadán žádný parametr pro hledání
        else:

            # Nastavení hodnoty atributu záznam o prázdném dotazu
            self.empty_query = True

            # Vytvoření popisného textu a prázdného seznamu ID
            self.display_text = "No search parameters were provided."
            self.article_ids = []

        # Získání a navrácení článků z databáze dle ID nalezených ve schématu
        queryset = Article.objects.filter(id__in=self.article_ids)
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


    def search_navigation_check(self):
        '''
        Metoda pro ověření, zda má uživatel zapnutou navigaci pro zobrazení podobných článků na základě tagů.

        Tato metoda získává přihlášeného uživatele z aktuálního požadavku a ověřuje, zda je uživatel přihlášený
        a má zapnutou navigaci pro zobrazení podobných článků na základě tagů. Pokud je to pravda, vrátí True,
        jinak vrátí False.

        :return: True, pokud je navigace zapnutá, jinak False.
        '''

        # Ověření zda uživatel má zaplé zobrazení navigace pro podobné články
        if self.user.show_tab_for_similar:
            return True
        return False


    def get_context_data(self, **kwargs):
        '''
        Metoda pro vytvoření kontextu pro šablonu.

        Tato metoda vytváří kontext pro šablonu, který obsahuje data, která jsou použita k vykreslení stránky.
        Nejprve získá běžný kontext voláním nadřazené metody `super().get_context_data(**kwargs)`.
        Poté přidává další informace do kontextu jako je jméno URL, dotaz z vyhledávání, potvrzení pro skrytí navigace,
        text s popisem výsledku vyhledávání a další.

        :param kwargs: Klíčové argumenty, které mohou být předány metodě.
        :return: Kontext s vloženými daty pro šablonu.
        '''

        # Získání běžného kontextu
        context = super().get_context_data(**kwargs)

        # Přidání jména URL
        context['url_name'] = self.url_name

        # Přidání dotazu
        query = self.kwargs.get('query') or self.request.GET.get('q')
        context['search_query'] = query

        # Přidání potvrzení pro skyrí navigace pokud je zadán prázdný dotaz
        context['empty_query'] = self.empty_query

        # Přidání textu s popisem výsledku vyhledávání
        context['display_text'] = self.display_text
        print("### self.display_text", self.display_text)

        # pokud má uživatel zapnutou navigaci pro podobné články
        if self.search_navigation_check():

            # Přidání seznamu zobrazených kategorií
            context['category_items'] = self.category_items

            # Přidání aktuálně vybrané kategorie
            context['current_category_slug'] = self.current_category_tab['slug']

        # Navrácení kontextu
        return context
