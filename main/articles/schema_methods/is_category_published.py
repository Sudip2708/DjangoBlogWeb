from whoosh.query import Term
from articles.schema import ArticleSchema


def is_category_published(category_id):
    '''
    Zjišťuje, zda má alespoň jeden článek v dané kategorii status 'publish'.

    :param category_id: ID kategorie.
    :return: True, pokud má alespoň jeden článek status 'publish', jinak False.
    '''

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:

        # Vytvoření dotazu pro hledání článků dané kategorie
        query = Term("category", str(category_id))

        # Vyhledání článků
        results = searcher.search(query)

        # Procházení nalezených článků
        for hit in results:

            # Pokud je nalezen článek s statusem 'publish', vrátí True
            if hit['status'] == 'publish':
                return True

    # Pokud nebyl nalezen žádný článek s statusem 'publish', vrátí False
    return False