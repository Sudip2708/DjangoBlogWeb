from whoosh.query import Term
from ....models.article_author import ArticleAuthor


def search_in_author(author_id):
    '''
    Function for creating a query and descriptive text for searching articles by author.

    The function receives the author's ID and creates a query for searching in the schema index
    based on that ID, along with a descriptive text indicating that the search was performed by author.

    The function returns the created query and descriptive text.
    '''

    # Creating the query
    author_query = Term('author', author_id)

    # Creating descriptive text for the search result
    author_name = ArticleAuthor.objects.get(id=author_id).name
    display_text = f"written by the author {author_name}"

    return author_query, display_text
