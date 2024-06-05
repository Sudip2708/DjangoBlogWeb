def print_indexed_articles(self):
    '''
    Method of the ArticleSchema class for printing the titles of all indexed articles.

    First, the method creates an empty list for the titles of indexed articles.
    Then, it loads the searcher within the Whoosh schema
    and iterates through to create a list of titles of all indexed articles.

    The method prints to the terminal
    the list of titles of all indexed articles.
    '''

    # List for article titles
    article_titles = []

    # Search for article titles
    with self.ix.searcher() as searcher:
        for doc in searcher.documents():
            article_titles.append(doc['title'])

    # Print article titles
    print("Indexed Articles:")
    for title in article_titles:
        print(title)
