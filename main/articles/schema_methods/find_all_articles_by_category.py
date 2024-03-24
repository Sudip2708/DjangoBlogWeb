
from articles.schema import ArticleSchema


def find_all_articles_by_category(category_ID):
    '''
    Vyhledá a vrátí seznam ID článků daného stavu seřazených podle data publikování.

    :param category_ID: Stav článků pro vyhledání (např. 'publish').
    :return: Seznam ID článků.
    '''

    # Seznam pro výsledné ID článků
    article_ids = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:
        results = searcher.documents(category=category_ID)

        # Procházení výsledků a přidání ID článků do seznamu
        for doc in results:
            article_ids.append(doc['id'])

    # Navrácení seznamu ID článků
    return article_ids
