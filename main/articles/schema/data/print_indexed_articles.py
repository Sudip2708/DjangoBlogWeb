def print_indexed_articles(self):
    '''
    Metoda třídy ArticleSchema pro vytisknutí názvů všech indexovaných článků.

    Nejprve metoda vytvoří prázdný seznam pro názvy indexovaných článků.
    Následně načte vyhledávač ve Whoosh schématu
    a cyklem vytvoří seznam názvů všech indexovaných článků.

    Metoda vrací tiskem do terminálu
    seznam všech názvů indexovaných článků.
    '''

    # Seznam pro názvy článků
    article_titles = []

    # Vyhledání názvů článků
    with self.ix.searcher() as searcher:
        for doc in searcher.documents():
            article_titles.append(doc['title'])

    # Tisk názvů článků
    print("Indexované články:")
    for title in article_titles:
        print(title)
