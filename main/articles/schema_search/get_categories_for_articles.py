
from articles.schema import ArticleSchema
from articles.models.article_category import ArticleCategory




def get_categories_for_articles(article_ids):
    '''
    Metoda pro získání kategorií pro zadané články.

    Tato metoda přijímá seznam ID článků `article_ids` a získává kategorie, ke kterým tyto články patří.
    Následně vrací seznam kategorií ve formě slovníků obsahujících identifikátor kategorie (`id`), její slug (`slug`) a název (`title`).

    :param article_ids: Seznam ID článků, pro které se získávají kategorie.
    :return: Seznam slovníků reprezentujících kategorie, ke kterým články patří.
    '''

    # Inicializace prázdného seznamu pro kategorie
    category_ids = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:

        # Procházení článků podle jejich ID
        for article_id in article_ids:

            # Získání dokumentu z indexu se schématem
            document = searcher.document(id=str(article_id))

            # Přidání kategorie z dokumentu do seznamu
            category_ids.append(document['category'])

    # Odstranění duplicitních kategorií a vytvoření seznamu
    category_ids = list(set(category_ids))

    # Získání názvů kategorií pomocí seznamu ID kategorií
    category_items = ArticleCategory.objects.filter(id__in=category_ids).values('id', 'slug', 'title')

    # Navrácení seznamu kategorií
    return category_items