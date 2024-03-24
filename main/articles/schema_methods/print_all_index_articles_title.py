from articles.schema import ArticleSchema

def print_all_index_articles_title():
    '''
    Metoda pro výpis názvů všech indexovaných článků.

    Tato metoda prochází všechny dokumenty v indexu a vytiskne názvy článků.

    :return: None
    '''

    # Inicializace seznamu názvů článků
    article_titles = []

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Načtení vyhledávače ve Vhoosh schématu
    with article_schema.ix.searcher() as searcher:

        # Vytáhnutí všech dokumentů
        results = searcher.documents()

        # Pro každý dokument získání názvu článku a přidání do seznamu
        for doc in results:
            article_titles.append(doc['author'])

    # Vytisknutí seznamu názvů článků
    print("Indexované články:")
    for title in article_titles:
        print(title)