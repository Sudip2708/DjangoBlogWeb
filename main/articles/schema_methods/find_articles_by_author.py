from articles.schema import ArticleSchema


def find_articles_by_author(author_name):
    '''
    Vyhledá a vrátí seznam ID článků daného autora.

    :param author_name: Jméno autora (string).
    :return: Seznam ID článků.
    '''

    # Normalizace jména autora na malá písmena
    normalized_author_name = author_name.lower()

    # Inicializace seznamu názvů článků
    article_id = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:

        # Vytáhnutí všech dokumentů
        results = searcher.documents()

        # Pro každý dokument získání názvu článku a přidání do seznamu
        for doc in results:
            if doc['author'] == normalized_author_name:
                article_id.append(doc['id'])

    return article_id