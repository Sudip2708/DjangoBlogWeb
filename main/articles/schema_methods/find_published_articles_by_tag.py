from whoosh.query import Term
from articles.schema import ArticleSchema


def find_published_articles_by_tag(tag_id):
    '''
    Vyhledá články s daným tagem, které mají status publish.

    :param tag_id: ID tagu
    :return: Seznam ID článků
    '''

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:

        # Vytvoření dotazu pro hledání článků s daným tagem a statusem publish
        query = Term("tags", str(tag_id)) & Term("status", "publish")

        # Vyhledání článků
        results = searcher.search(query)

        # Seznam ID nalezených článků
        article_ids = [int(hit["id"]) for hit in results]

    # Navrácení seznamu ID článků
    return article_ids