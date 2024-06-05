from whoosh import sorting
from whoosh.query import And

from ...schema.article_schema import ArticleSchema
from .get_article_ids_data.search_in_query import search_in_query
from .get_article_ids_data.search_in_date import search_in_date
from .get_article_ids_data.search_in_author import search_in_author


def get_article_ids(search_parameters):
    '''
    Function for obtaining article IDs based on the provided search parameters.

    The function accepts a dictionary `search_parameters`, which contains search parameters.

    The function first defines variables `query` and `display_text` for creating a query and descriptive text,
    announcing what data was searched for. It then checks if a search query was provided.
    If so, it calls the function to create a query and descriptive text for this field.
    Then it checks if a date was specified for article publication.
    If so, it calls the function to create a query and descriptive text for this field.
    Then it checks if an author was specified.
    If so, it calls the function to create a query and descriptive text for this field.

    Then it performs a search for articles in the index schema and creates a set of unique article IDs.

    The function returns a list of article IDs and a text describing the search content.
    '''

    # Definition of variables for creating a query and descriptive text
    query = None
    display_text = ""

    # If a search term is provided
    search_therm = search_parameters['query']
    search_fields = [i for i in ('title', 'overview', 'content') if search_parameters[i]]
    if search_therm:
        term_query, term_text = search_in_query(search_therm, search_fields)
        query = term_query
        display_text += term_text

    # If a search parameter for date is provided
    before_date = search_parameters['before']
    after_date = search_parameters['after']
    if before_date or after_date:
        date_query, date_text = search_in_date(before_date, after_date)
        query = date_query if query is None else And([query, date_query])
        display_text += date_text

    # If a search parameter for author is provided
    author_id = search_parameters['author']

    if author_id:
        author_query, author_text = search_in_author(author_id)
        query = author_query if query is None else And([query, author_query])
        display_text += author_text

    # Searching the Whoosh query and obtaining article IDs
    with ArticleSchema().ix.searcher() as searcher:
        results = searcher.search(query, sortedby=sorting.FieldFacet('published', reverse=True))
        article_ids = [int(hit['id']) for hit in results]

    # Returning article IDs and the text to be displayed
    return article_ids, display_text
