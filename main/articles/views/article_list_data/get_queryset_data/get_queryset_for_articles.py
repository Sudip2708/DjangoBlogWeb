from ....models.article import Article
from ....models.article_category import ArticleCategory


def get_queryset_for_articles(self):
    '''
    Metoda pro vytvoření seznamu článků pro stránku se všemi články.

    Metoda je určená pro tyto URL:
    - article-list: Stránka zobrazující všechny publikované články.

    Atributy přidané nebo měněné touto metodou:
    - self.category_tabs: Seznam všech publikovaných kategorií.
    - self.current_category: Data pro aktuální záložku.
    - self.page_title: Název stránky.
    - self.page_title_mobile: Název stránky pro mobilní zařízení.
    - self.page_subtitle: Podnázev stránky (zobrazí se, když je navigace pro kategorie skrytá).

    Metoda nejprve ověří, zda má uživatel zapnuté zobrazení navigace pro kategorie.
    Pokud ano, vytvoří atributy self.category_tabs, self.current_category, self.page_title a self.page_title_mobile.
    Pokud ne, vytvoří atributy self.page_title, self.page_title_mobile, self.page_subtitle.

    Metoda vyhledá a vrací všechny publikované články.
    (Články jsou seřazeny od nejnovějšího po nejstarší.)
    '''

    # Vytvoření hodnot pro stránku se zapnutou navigací pro kategorie
    if self.user.settings.get('show_category_navigation'):
        self.category_tabs = ArticleCategory.objects.exclude(id=1)
        self.current_category = {'id': 0, 'slug': 'all', 'title': 'All'}
        self.page_title = 'Article Categories'
        self.page_title_mobile = 'All Articles'

    # Vytvoření hodnot pro stránku bez zapnuté navigace pro kategorie
    else:
        self.page_title = self.page_title_mobile = 'All Articles'
        self.page_subtitle = 'To see tab for categories click on Show Category in navbar.'

    # Vytvoření a navrácení instancí článků
    queryset = Article.objects.filter(status='publish') \
                              .order_by('-created')
    return queryset
