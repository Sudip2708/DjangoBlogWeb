from whoosh import sorting
from whoosh.query import And

from articles.schema import ArticleSchema
from .search_in_query import search_in_query
from .search_in_date import search_in_date
from .search_in_author import search_in_author



def get_article_ids_by_search_params(search_parameters):
    '''
    Metoda pro získání ID článků na základě zadaných parametrů hledání.

    Tato metoda přijímá slovník `search_parameters`, který obsahuje různé parametry pro hledání, jako je hledaný výraz, datum a autor.
    Poté vytváří dotazy pro hledání na základě těchto parametrů a provádí vyhledávání pomocí Whoosh.
    Nakonec vrací seznam ID článků odpovídajících hledání a popisný text výsledku vyhledávání.

    :param search_parameters: Slovník obsahující různé parametry pro hledání, jako je hledaný výraz, datum a autor.
    :return: Tuple obsahující seznam ID článků odpovídajících hledání a popisný text výsledku vyhledávání.
    '''

    # Deklarace proměných
    term_query = date_query = author_query = None
    term_text = date_text = author_text = ""

    # Pokud je zadán hledaný výraz
    if search_parameters['query']:
        term_query, term_text = search_in_query(search_parameters)

    # Pokud e zadán paremetr hledání podle data
    if search_parameters['before'] or search_parameters['after']:
        date_query, date_text = search_in_date(search_parameters)

    # Pokud e zadán paremetr hledání podle autora
    if search_parameters['author']:
        author_query, author_text = search_in_author(search_parameters)

    # Vytvoření společného dotazu
    queries = [i for i in (term_query, date_query, author_query) if i]
    if queries:
        query = queries[0] if len(queries) == 1 else And(queries)
    else:
        query = None

    # Vyhledání dotazu Whoosh a získání ID článků
    if query:

        # Získání Whoosh schématu
        article_schema = ArticleSchema()

        # Načtení vyhledávače ve Vhoosh schématu
        with article_schema.ix.searcher() as searcher:

            # Získání výsledku na základě dotazu a řazené podle data poslední úpravy
            results = searcher.search(query,sortedby=sorting.FieldFacet('updated', reverse=True))

            # Získání ID článků
            article_ids = [int(hit['id']) for hit in results]

    # Vytvoření společného popisného textu
    display_text = term_text + date_text + author_text

    # Navrácení ID článku a textu který se má zobrazit
    return (article_ids, display_text)