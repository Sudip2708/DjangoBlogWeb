import ast

from ...models.article import Article
from ..common_data.get_similar_data import get_similar_data
from ..common_data.get_category_data import get_category_data
from .get_article_ids import get_article_ids


def get_queryset(self):
    '''
    Metoda slouží k získání obsahu na základě zadaného hledání.

    Metoda je určená pro tyto URL:
    - article-search-results: Stránka pro zobrazení výsledků vyhledávání.
    - article-search-similar: Stránka pro zobrazení podobných článků pro články z výsledku vyhledávání.
    - article-search-results-category: Stránka pro zobrazení kategorií pro výsledek vyhledávání.
    - article-search-similar-category: Stránka pro zobrazení kategorií pro podobné články.

    Atributy přidané nebo měněné touto metodou:
    - self.search_parameters: Atribut obsahující slovník s parametry dotazu.
    - self.article_ids: Atribut pro ID článku na základě hledaných dat.
    - self.page_title: Atribut pro nadpis stránky.
    - self.page_title_mobile: Název stránky pro mobilní zařízení.
    - self.display_text: Atribut pro popisný text, informující o tom, co bylo hledáno.
    - self.info_text: Informační text (zobrazí se, když není nalezen žádný podobný článek).
    - self.category_items: Atribut pro výčet kategorií pro výsledek hledání.
    - self.current_category_tab: Atribut pro aktuálně vybranou záložku kategorie.

    Metoda nejprve načte parametry hledání a vytvoří pro ně atribut self.search_parameters.

    Po té volá funkci pro vyhledání obsahu na základě parametrů hledání,
    která vrací obsah pro atribut self.article_ids a self.display_text.

    Následně vytvoří nadpis pro mobilní zařízení.

    Metoda po té ověří, zda požadavek přišel z adresy pro zobrazení výsledků pro parametry hledání,
    (url name začíná řetězcem 'article-search-results')
    a pokud ano, vytvoří obsah pro atribut self.page_title.

    Následně metoda ověří, zda požadavek přišel z adresy pro zobrazení podobných článků,
    (url name začíná řetězcem 'article-search-similar')
    a pokud ano, je volána metoda, která na základě atributu self.article_ids vyhledá články,
    které mají alespoň jeden shodný tag a nejsou obsaženy v self.article_ids.
    A po té přepíše tento atribut novými hodnotami.

    Dále metoda ověří, zda požadavek přišel s adresy pro zobrazení kategorií
    (koncový část jména adresy obsahuje řetězec 'category').
    Pokud ano, volá metodu pro získání seznamu kategorií
    a obsahu pro aktuálně zobrazenou kategorii:
    self.article_ids, self.category_items a self.current_category_tab.

    Nakonec metoda ještě zkontroluje, zda nově obsah pro self.article_ids
    obsahuje alespoň jeden záznam, a pokud ne, vytvoří atribut self.info_text.

    Metoda nakonec vyhledá a vrací instance článků dle obsahu atributu self.article_ids.
    (Články jsou seřazeny od nejnovějšího po nejstarší.)
    '''

    # Nastavení pro stránku s výpisem chyb
    if self.url_name == 'article-search-error':
        return Article.objects.none()

    # Získání parametrů pro hledání
    self.search_parameters = ast.literal_eval(self.kwargs.get('query'))

    # Získání ID článků a popisného textu dle zadaných parametrů
    self.article_ids, self.display_text = get_article_ids(self.search_parameters)

    # Nastavení názvu zobrazeného na mobilních zařízeních
    self.page_title_mobile = 'Search results'

    # Vytvoření nadpisu stránky
    if self.url_name.startswith('article-search-results'):
        self.page_title = 'Search results for Articles'

    # Získání ID článků a nadpisu pro stránku s podobnými články dle tagů
    if self.url_name.startswith('article-search-similar'):
        get_similar_data(self)
        self.page_title = 'Similar Articles for Search Result'

    # Získání ID článků pro stránky se zobrazenými kategoriemi
    if self.url_name.endswith('category'):
        get_category_data(self)

    # Vytvoření oznamu, pokud není nalezen žádný článek
    if not self.article_ids:
        self.info_text = 'There are no articles for this request.'

    # Vytvoření a navrácení seznamu instancí vybraných článků
    queryset = Article.objects.filter(id__in=self.article_ids)
    return queryset
