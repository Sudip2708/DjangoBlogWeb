from whoosh.query import Term

from articles.schema import ArticleSchema
from .get_categories_for_articles import get_categories_for_articles


def get_category_articles_ids(article_ids, current_category_tab_slug):
    '''
    Metoda pro získání ID článků a aktuální kategorie na základě zadaných parametrů.

    Tato metoda přijímá seznam ID článků `article_ids` a slug aktuální kategorie `current_category_tab_slug`.
    Prochází články podle jejich ID a hledá ty, které patří do zadané kategorie. Pokud není specifikována žádná kategorie
    nebo žádné články neodpovídají aktuální kategorii, vrátí články ze standardní kategorie.
    Následně vrací seznam ID nalezených článků, informace o aktuální kategorii a seznam všech kategorií, ke kterým patří nalezené články.

    :param article_ids: Seznam ID článků, pro které se provádí hledání.
    :param current_category_tab_slug: Slug aktuální kategorie.
    :return: Tuple obsahující seznam ID nalezených článků, informace o aktuální kategorii a seznam všech kategorií, ke kterým patří nalezené články.
    '''

    # Získání seznamu slovníku pro kategorie
    # [{'id': 1, 'slug': 'category1-slug', 'title': 'Category 1 Title'},]
    category_items = get_categories_for_articles(article_ids)

    # Získání aktuální kategorie ze seznamu (je-li)
    current_category = None
    for item in category_items:
        if item['slug'] == current_category_tab_slug:
            current_category = item

    # Pokud v seznamu kategorie není, použij první ze seznamu
    if not current_category:
        current_category = category_items[0]

    # Získání ID aktuální kategorie
    category_id = current_category['id']

    # Inicializace seznamu pro výstup
    matching_article_ids = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Otevření vyhledávače
    with article_schema.ix.searcher() as searcher:

        # Procházení článků podle jejich ID
        for article_id in article_ids:

            # Vytvoření dotazu pro vyhledání článku s daným ID a kategorií
            query = Term("id", str(article_id)) & Term("category", str(category_id))

            # Vyhledání článku
            results = searcher.search(query)

            # Pokud byl nalezen článek, přidej jeho ID do výstupu
            if results:
                matching_article_ids.append(article_id)

    # Navrácení nalezených ID článků, aktuální kategorie a seznamu kategorií pro nalezená ID článků
    return (matching_article_ids, current_category, category_items)
