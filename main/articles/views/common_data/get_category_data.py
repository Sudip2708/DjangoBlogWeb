from ...models.article import Article
from ...models.article_category import ArticleCategory

def get_category_data(self):
    '''
    Metoda pro vytvoření seznamu článků pro konkrétní kategorii.

    Metoda je použita v těchto souborech:
    - articles/views/article_list_data/get_queryset_data/get_queryset_for_tags.py
    - articles/views/search_data/get_queryset.py

    Atributy přidané nebo měněné touto metodou:
    - self.article_ids: ID článků které obsahují vybraný tag.
    - self.current_category: Instance aktuálně vybrané kategorie.
    - self.category_tabs = Instance kategorií pro self.article_ids.
    - self.page_title: Název stránky.

    Metoda nejprve načte z adresy slug aktuálně vybrané kategorie.

    Metoda následně vyhledá na základě ID článků množinu ID kategorií,
    po té vyhledá instance kategorií na základě jejich ID,
    a přidá je do atributu self.category_tabs.

    Po té na základě hodnoty pro current_category provede kontrolu,
    zda některá z kategorií obsahuje stejný slag,
    jako je uveden v této proměné a při shodě načte tuto kategorii do atributu self.current_category.
    V případě neshody (mhodnota current_category může obsahovat i řetězec 'first'
    použitý v případě prvního zobrazení navigace pro kategorie,
    kdy chceme získat seznam pro první záložku, ale ještě nevíme jaká to bude),
    nastaví jako vybranou kategorii první v seznamu.

    Nakonec pro tuto vybranou kategorii vyfiltruje z atributu self.article_ids ty články,
    které spadají do této kategorie a přepíše s nimi obsah atributu.

    Nakonec metoda vytvoří atribut self.page_title pro název stránky.
    '''

    # Načtení aktuální kategorie
    current_category = self.kwargs['category_slug']

    # Získání množiny ID kategorií na základě ID článků
    article_category_ids = Article.objects \
        .filter(id__in=self.article_ids) \
        .values_list('category_id', flat=True) \
        .distinct()

    # Získání množiny instancí kategorií na základě ID kategorií
    self.category_tabs = ArticleCategory.objects \
        .filter(id__in=article_category_ids) \
        .distinct()

    # Získání kategorie, která bude zobrazena po načtení stránky
    self.current_category = next(
        (category for category in self.category_tabs if category.slug == current_category),
        self.category_tabs.first()
    )

    # Získání seznamu ID článků s stavem "publish" a navázaných na danou kategorii
    self.article_ids = Article.objects \
        .filter(id__in=self.article_ids, category=self.current_category) \
        .values_list('id', flat=True)

    # Vytvoření nadpisu stránky
    self.page_title = f'Category for {self.page_title}'