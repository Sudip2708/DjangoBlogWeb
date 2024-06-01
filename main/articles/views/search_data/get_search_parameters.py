def get_search_parameters(form_cleaned_data):
    '''
    Funkce pro zpracování očištěných dat získaných z formuláře.

    Funkce nejprve vytvoří slovník s parametry hledání z očištěných dat získaných z formuláře.
    Pokud jsou v datech uvedeny hodnoty dat, převede je do požadovaného formátu.
    Pokud je v datech uvedena instance autora, převede ji na jeho ID.

    Funkce vrací slovník se zpracovanými daty.
    '''

    # Získání slovníku z dat formuláře
    search_parameters = {
        'query': form_cleaned_data.get('query'),
        'title': form_cleaned_data.get('search_in_title'),
        'overview': form_cleaned_data.get('search_in_description'),
        'content': form_cleaned_data.get('search_in_content'),
        'before': form_cleaned_data.get('date_to'),
        'after': form_cleaned_data.get('date_from'),
        'author': form_cleaned_data.get('author')
    }

    # Převod data na formát 'yyyy-mm-dd'
    if search_parameters['before']:
        formatted_date = search_parameters['before'].strftime("%Y-%m-%d")
        search_parameters['before'] = formatted_date

    # Převod data na formát 'yyyy-mm-dd'
    if search_parameters['after']:
        formatted_date = search_parameters['after'].strftime("%Y-%m-%d")
        search_parameters['after'] = formatted_date

    # Převod instance autora na jeho ID
    if search_parameters['author']:
        author_id = search_parameters['author'].id
        search_parameters['author'] = str(author_id)

    return search_parameters
