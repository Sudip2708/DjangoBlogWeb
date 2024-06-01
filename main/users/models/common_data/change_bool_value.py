def change_bool_value(dictionary, field_key):
    '''
    Funkce pro změnu boolean hodnot ve slovníku.

    Funkce obdrží slovník s příslušnými daty a klíč,
    dle kterého následně ve slovníku vyhledá zápis
    a změní bool hodnotu na její opak.

    Funkce vrací slovník s aktualizovanými daty.
    '''

    try:
        dictionary[field_key] = not dictionary[field_key]
        return dictionary

    except Exception as e:
        print(f"###ERROR### change_sidebar_bool_value: {e}")
