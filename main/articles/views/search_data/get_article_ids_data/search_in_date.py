from whoosh.query import DateRange
from dateutil.parser import parse as parse_date


def search_in_date(before_date, after_date):
    '''
    Funkce pro vytvoření dotazu a popisného textu pro hledání článků podle data.

    Funkce obdrží řetězec ve formátu 'yyyy-mm-dd' pro datum před a po.

    Následně tyto řetězce převede na objekt datetime (nebo hodnotu None)
    a použije je pro vytvoření dotazu pro hledání v indexu schématu,
    a poté vytvoří popisný text dle parametrů hledání.

    Funkce vrací vytvořený dotaz a popisný text.
    '''

    # Převod zadaných hodnot na objekty datetime nebo None
    parse_before = parse_date(before_date) if before_date else None
    parse_after = parse_date(after_date) if after_date else None

    # Vytvoření dotazu
    date_query = DateRange("published",
                           parse_after, parse_before,
                           startexcl=False, endexcl=False )

    # Vytvoření popisného textu pro výsledek hledání
    display_text = ""
    if before_date:
        display_text += f"published before {parse_before.strftime('%d. %m. %Y')}"
        if after_date:
            display_text += f" and after {parse_after.strftime('%d. %m. %Y')}"
    elif after_date:
        display_text += f"published after {parse_after.strftime('%d. %m. %Y')}"
    display_text += "<br>"

    return date_query, display_text
