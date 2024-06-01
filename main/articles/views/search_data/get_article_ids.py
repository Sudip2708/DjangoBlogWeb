from whoosh import sorting
from whoosh.query import And

from ...schema.article_schema import ArticleSchema
from .get_article_ids_data.search_in_query import search_in_query
from .get_article_ids_data.search_in_date import search_in_date
from .get_article_ids_data.search_in_author import search_in_author


def get_article_ids(search_parameters):
    '''
    Funkce pro získání ID článků na základě zadaných parametrů hledání.

    Funkce přijímá slovník `search_parameters`, který obsahuje parametry pro hledání.

    Funkce nejprve definuje proměnné `query` a `display_text` pro vytvoření dotazu a popisného textu,
    který oznamuje, jaká data byla hledána. Následně zkontroluje, zda byl zadán dotaz pro vyhledávání.
    Pokud ano, volá funkci pro vytvoření dotazu a popisného textu pro toto pole.
    Poté zkontroluje, zda bylo zadáno datum pro specifikaci publikování článku.
    Pokud ano, volá funkci pro vytvoření dotazu a popisného textu pro toto pole.
    Poté zkontroluje, zda byl zadán autor.
    Pokud ano, volá funkci pro vytvoření dotazu a popisného textu pro toto pole.

    Následně provede vyhledání článků v indexovém schématu a vytvoří množinu jedinečných ID článků.

    Funkce vrací seznam ID článků a text popisující obsah vyhledávání.
    '''

    # Definice proměnných pro vytvoření dotazu a popisného textu
    query = None
    display_text = ""

    # Pokud je zadán hledaný výraz
    search_therm = search_parameters['query']
    search_fields = [i for i in ('title', 'overview', 'content') if search_parameters[i]]
    if search_therm:
        term_query, term_text = search_in_query(search_therm, search_fields)
        query = term_query
        display_text += term_text

    # Pokud je zadán parameter hledání podle data
    before_date = search_parameters['before']
    after_date = search_parameters['after']
    if before_date or after_date:
        date_query, date_text = search_in_date(before_date, after_date)
        query = date_query if query is None else And([query, date_query])
        display_text += date_text

    # Pokud je zadán parameter hledání podle autora
    author_id = search_parameters['author']

    if author_id:
        author_query, author_text = search_in_author(author_id)
        query = author_query if query is None else And([query, author_query])
        display_text += author_text

    # Vyhledání dotazu Whoosh a získání ID článků
    with ArticleSchema().ix.searcher() as searcher:
        results = searcher.search(query, sortedby=sorting.FieldFacet('published', reverse=True))
        article_ids = [int(hit['id']) for hit in results]

    # Návrat ID článků a textu, který se má zobrazit
    return article_ids, display_text
