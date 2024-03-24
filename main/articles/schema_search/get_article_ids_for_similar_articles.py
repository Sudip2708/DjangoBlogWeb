from taggit.models import Tag
from articles.schema import ArticleSchema



def get_article_ids_for_similar_articles(article_ids):
    '''
    Metoda pro získání ID článků pro podobné články na základě zadaných ID článků.

    Tato metoda přijímá seznam ID článků `article_ids` a hledá články s podobnými tagy v Whoosh indexu.
    Poté vrací seznam ID článků, které jsou podobné článkům zadaným v parametru.

    :param article_ids: Seznam ID článků, pro které se hledají podobné články.
    :return: Seznam ID článků, které jsou podobné článkům zadaným v parametru.
    '''

    # Získání tagů článků na aktuální stránce
    current_article_tags = Tag.objects.filter(article__id__in=article_ids)

    # Vytvoření dotazu pro hledání podobných článků v Whoosh indexu
    similar_article_ids = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:

        # Nalezení všech článků se stejnými tagy
        for tag in current_article_tags:
            similar_results = searcher.documents(tags=str(tag.id))
            similar_article_ids.extend(int(hit['id']) for hit in similar_results)

    # Odstranění ID článků nalezených podle dotazu z výsledných ID článků
    article_ids = list(set(similar_article_ids) - set(article_ids))

    # Navrácení ID článků
    return article_ids