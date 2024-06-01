from django.shortcuts import get_object_or_404

from ....models.article import Article
from ....models.article_category import ArticleCategory

def get_queryset_for_categories(self):
    '''
    Metoda pro vytvoření seznamu článků pro vybranou kategorii.

    Metoda je určená pro tyto URL:
    - article-category-list: Stránka zobrazující všechny publikované články roztříděné do kategorií.

    Atributy přidané nebo měněné touto metodou:
    - self.current_category: Aktuálně vybraná kategorie
    - self.category_tabs: Seznam všech publikovaných kategorií.
    - self.page_title: Název stránky.
    - self.page_title_mobile: Název stránky pro mobilní zařízení.
    - self.page_subtitle: Podnázev stránky (zobrazí se, když je navigace pro kategorie skrytá).

    Metoda nejprve načte z adresy slug aktuálně vybrané kategorie,
    a po té získá její instanci a uloží ji jako atribut self.current_category.
    (V případě, že nebude nalezena kategorie pro daný slug, vyvolá se výjimka 404.)

    Metoda následně ověří, jestli má uživate zapnuté zbrazení navigace pro kategorie.
    Pokud ano, vytvoří atributy self.category_tabs, self.page_title a self.page_title_mobile.
    Pokud ne, vytvoří atributy self.page_title, self.page_title_mobile a self.page_subtitle.

    Metoda vyhledá a vrací všechny publikované články pro danou kategorii.
    (Články jsou seřazeny od nejnovějšího po nejstarší.)
    '''

    # Načtení aktuální kategorie
    current_category_slug = self.kwargs['category_slug']
    self.current_category = get_object_or_404(ArticleCategory, slug=current_category_slug)

    # Vytvoření hodnot pro stránku se zapnutou navigací pro kategorie
    if self.user.settings.get('show_category_navigation'):
        self.category_tabs = ArticleCategory.objects.exclude(id=1)
        self.page_title = 'Article Categories'
        self.page_title_mobile = f'Category: {self.current_category.name}'

    # Vytvoření hodnot pro stránku bez zapnuté navigace pro kategorie
    else:
        self.page_title = f'Articles for Category: {self.current_category.name}'
        self.page_title_mobile = f'Category: {self.current_category.name}'
        self.page_subtitle = 'To see tab for categories click on Show Category in navbar.'

    # Vytvoření a návrácení instancí článků
    queryset = Article.objects.filter(category=self.current_category, status='publish') \
                              .order_by('-created')
    return queryset
