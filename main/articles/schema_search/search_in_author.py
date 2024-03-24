from whoosh.query import And, Term
from articles.models.article_author import ArticleAuthor


def search_in_author(search_parameters):
    '''
    Metoda pro hledání podle autora.

    Tato metoda zpracovává hledání podle autora.
    Získává ID autora z parametrů hledání a vytváří dotaz, který vyhledává články napsané tímto autorem.
    Výsledný dotaz a popisný text pro výsledek hledání jsou pak vráceny.

    :param search_parameters: Slovník obsahující parametry hledání.
    :return: Tuple obsahující dotaz a popisný text pro výsledek hledání.
    '''

    #Získání ID autora
    author_id = search_parameters['author']

    # Vytvoření dotazu
    author_query = Term('author', str(author_id))

    # Vytvoření popisného textu pro výsledek hledání
    author_name = ArticleAuthor.objects.get(id=author_id).author
    display_text = f"written by the author {author_name}"

    # Navrácení dotazu a popisného textu k zobrazení
    return (author_query, display_text)