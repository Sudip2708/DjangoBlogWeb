from whoosh.qparser import MultifieldParser
from whoosh.query import Or

from ....schema.article_schema import ArticleSchema


def search_in_query(search_term, search_fields):
    '''
    Function for creating a query and descriptive text for searching articles based on the provided query.

    The function takes the search term and a list of fields intended for searching.
    It first creates an instance of the index schema
    and then checks if the search term contains spaces (i.e., words).
    If it does, it splits those words and creates a query for each word and field intended for searching,
    and descriptive text that is a combination of these words.
    If it does not contain spaces, it creates a query for the given word and fields intended for searching,
    and descriptive text for the given word.
    Finally, it checks if all fields for searching are selected,
    if not, it adds a mention of the fields where the search was conducted to the text.

    The function returns the created query and descriptive text.
    '''

    # Getting the Whoosh schema
    article_schema = ArticleSchema()

    # Checking if the search term contains at least one space
    if ' ' in search_term:

        # Splitting the search term into individual words
        search_words = search_term.split()

        # Creating a query for each word separately and combining them using the OR operator
        parser = MultifieldParser(search_fields, schema=article_schema.get_schema())
        term_queries = [parser.parse(word) for word in search_words]
        query = Or(term_queries)

        # Creating descriptive text for the search result
        display_text = f"with the terms: {' '.join(search_words)}"

    # If the search term does not contain a space, use the original
    else:

        # Creating a query for the entire search term
        parser = MultifieldParser(search_fields, schema=article_schema.get_schema())
        query = parser.parse(search_term)

        # Creating descriptive text for the search result, if only specific fields are selected
        display_text = f"with the term {search_term}"

    # Adding a description of the searched fields if not all fields are selected
    if len(search_fields) == 1:
        display_text += f" in {search_fields[0]}"
    elif len(search_fields) == 2:
        display_text += f" in {search_fields[0]} and {search_fields[1]}"
    display_text += "<br>"

    return query, display_text
