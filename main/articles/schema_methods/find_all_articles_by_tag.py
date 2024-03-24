
from articles.schema import ArticleSchema


def find_all_articles_by_tag(tag_ID):
    '''
    Vyhledá a vrátí seznam ID článků s daným tagem seřazených podle data publikování.

    :param tag_ID: ID tagu pro vyhledání.
    :return: Seznam ID článků.
    '''

    # Seznam pro výsledné ID článků
    article_ids = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:
        results = searcher.documents(tags=tag_ID)

        # Procházení výsledků a přidání ID článků do seznamu
        for doc in results:
            article_ids.append(doc['id'])

    # Navrácení seznamu ID článků
    return article_ids
