from whoosh.query import Term

from ....models.article_author import ArticleAuthor


def search_in_author(author_id):
    '''
    Funkce pro vytvoření dotazu a popisného textu pro hledání článků podle autora.

    Funkce obdrží ID autora a na jeho základě vytvoří dotaz pro hledání v indexu schématu
    a popisný text oznamující, že bylo hledáno podle autora.

    Funkce vrací vytvořený dotaz a popisný text.
    '''

    # Vytvoření dotazu
    author_query = Term('author', author_id)

    # Vytvoření popisného textu pro výsledek hledání
    author_name = ArticleAuthor.objects.get(id=author_id).name
    display_text = f"written by the author {author_name}"

    return author_query, display_text
