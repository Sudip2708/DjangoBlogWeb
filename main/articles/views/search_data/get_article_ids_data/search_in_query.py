from whoosh.qparser import MultifieldParser
from whoosh.query import Or

from ....schema.article_schema import ArticleSchema


def search_in_query(search_term, search_fields):
    '''
    Funkce pro vytvoření dotazu a popisného textu pro hledání článků na základě zadaného dotazu.

    Funkce přijímá hledaný termín a seznam polí určených k vyhledávání.
    Nejprve vytvoří instanci indexového schématu,
    a následně zkontroluje, zda hledaný termín obsahuje mezery (tj. slova).
    Pokud ano, rozdělí tato slova a vytvoří dotaz pro každé slovo a pole určených k vyhledávání,
    a popisný text, který je kombinací těchto slov.
    Pokud neobsahuje mezery, vytvoří dotaz pro dané slovo a pole určených k vyhledávání,
    a popisný text pro dané slovo.
    Nakonec zkontroluje, zda jsou vybraná všechna pole k hledání,
    pokud ne, doplní do textu zmínku o polích, ve kterých se hledalo.

    Funkce vrací vytvořený dotaz a popisný text.
    '''

    # Získání Whoosh schématu
    article_schema = ArticleSchema()

    # Kontrola, zda hledaný výraz obsahuje alespoň jednu mezeru
    if ' ' in search_term:

        # Rozdělení hledaného výrazu na jednotlivá slova
        search_words = search_term.split()

        # Vytvoření dotazu pro každé slovo zvlášť a spojení pomocí operátoru OR
        parser = MultifieldParser(search_fields, schema=article_schema.get_schema())
        term_queries = [parser.parse(word) for word in search_words]
        query = Or(term_queries)

        # Vytvoření popisného textu pro výsledek hledání
        display_text = f"with the terms: {' '.join(search_words)}"

    # Pokud hledaný výraz neobsahuje mezeru, použije se původní
    else:

        # Vytvoření dotazu pro celý hledaný výraz
        parser = MultifieldParser(search_fields, schema=article_schema.get_schema())
        query = parser.parse(search_term)

        # Vytvoření popisného textu pro výsledek hledání, pokud jsou vybrána jen některá pole
        display_text = f"with the term {search_term}"

    # Přidání popisu hledaných polí, pokud nejsou vybrána všechna pole
    if len(search_fields) == 1:
        display_text += f" in {search_fields[0]}"
    elif len(search_fields) == 2:
        display_text += f" in {search_fields[0]} and {search_fields[1]}"
    display_text += "<br>"

    return query, display_text