from whoosh.query import DateRange
from dateutil.parser import parse as parse_date
from datetime import datetime


def format_date(date):
    '''
    Metoda pro změnu formátu datumu

    :param date: Datum z formuláře (%Y-%m-%d)
    :return: Upravené datum (%d. %m. %Y)
    '''

    input_date = datetime.strptime(date, "%Y-%m-%d")
    return input_date.strftime("%d. %m. %Y")


def search_in_date(search_parameters):
    '''
    Metoda pro hledání v datumu.

    Tato metoda zpracovává hledání článků podle data jejich publikace.
    Pokud jsou zadány parametry pro hledání před a/nebo po určitém datu,
    vytváří se dotaz pro nalezení článků v daném rozmezí.
    Výsledný dotaz je vytvořen pomocí Whoosh schématu
    a zobrazení výsledku hledání je upraveno podle zadaných parametrů.

    :param search_parameters: Slovník obsahující parametry hledání.
    :return: Tuple obsahující dotaz a popisný text pro výsledek hledání.
    '''

    # Vytáhnutí zadané hodnoty a přiřazení do příslušné proměné
    before_date = parse_date(search_parameters['before']) if search_parameters['before'] else None
    after_date = parse_date(search_parameters['after']) if search_parameters['after'] else None

    # Vytvoření dotazu
    date_query = DateRange("updated", after_date, before_date, startexcl=False, endexcl=False )

    # Vytvoření popisného textu pro výsledek hledání
    display_text = ""

    # Jeli zadáno hledání před určitým datem
    if before_date:
        display_text += f"published before {format_date(search_parameters['before'])}"

        # Jeli zadáno i hledání po určitém datu
        if after_date:
            display_text += f" and after {format_date(search_parameters['after'])}"

    # Jeli zadáno pouze hledání po určitém datu
    elif after_date:
        display_text += f"published after {format_date(search_parameters['after'])}"

    # Přidání odskoku na další řádek
    display_text += "<br>"

    # Navrácení dotazu a popisného textu k zobrazení
    return (date_query, display_text)