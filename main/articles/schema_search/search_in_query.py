from whoosh.qparser import MultifieldParser
from articles.schema import ArticleSchema
from whoosh.query import Or


def search_in_query(search_parameters):
    '''
    Metoda pro vyhledávání hledaného výrazu v článcích.

    Tato metoda přijímá slovník `search_parameters`, který obsahuje různé parametry pro vyhledávání.
    Na základě těchto parametrů se vytváří dotaz pro vyhledávání v článcích.
    Pokud je hledaný výraz složen z více slov, rozdělí se na jednotlivá slova a vytvoří se dotazy pro každé slovo zvlášť,
    které se následně spojí operátorem OR.
    Pokud je hledaný výraz složen jen z jednoho slova, vytvoří se dotaz pro celý výraz.
    Výsledný dotaz a popisný text pro zobrazení jsou poté vráceny.

    :param search_parameters: Slovník obsahující parametry pro vyhledávání (např. hledaný výraz, pole hledání).
    :return: Dvojice obsahující dotaz pro vyhledávání a popisný text pro zobrazení.
    '''

    # Získání hledaného výrazu
    search_therm = search_parameters['query']

    # Získání polí v kterých se má výraz hledat
    search_fields = [i for i in ('title', 'overview', 'content') if search_parameters[i]]

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Kontrola, zda hledaný výraz obsahuje alespoň jednu mezeru
    if ' ' in search_therm:

        # Rozdělení hledaného výrazu na jednotlivá slova
        search_words = search_therm.split()

        # Vytvoření dotazu pro každé slovo zvlášť a spojení pomocí operátoru OR
        parser = MultifieldParser(search_fields, schema=article_schema.get_schema())
        term_queries = [parser.parse(word) for word in search_words]
        query = Or(term_queries)

        # Vytvoření popisného textu pro výsledek hledání
        display_text = f"with the terms: {' '.join(search_words)}"

    #  Pokud hledaný výraz neobsahuje mezeru, použije se původní
    else:

        # Vytvoření dotazu pro celý hledaný výraz
        parser = MultifieldParser(search_fields, schema=article_schema.get_schema())
        query = parser.parse(search_therm)

        # Vytvoření popisného textu pro výsledek hledání když jsou zaškrtnuta všechny pole
        display_text = f"with the therm {search_therm}"

    # Přidání popisu hledaných polí, pokud jsou zaškrtnuta jen některá
    if len(search_fields) == 1:
        display_text += f" in {search_fields[0]}"
    elif len(search_fields) == 2:
        display_text += f" in {search_fields[0]} and {search_fields[1]}"

    # Přidání odskoku na další řádek
    display_text += "<br>"

    # Navrácení dotazu a popisného textu k zobrazení
    return (query, display_text)