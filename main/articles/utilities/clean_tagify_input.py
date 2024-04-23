def clean_tagify_input(tags_input_value):
    '''
    Metoda na pročištění vstupních dat pro tagi

    Při vstupu z tagify jsou do databáze přidávané i následující znaky:
    ':', '[{', 'value', '{', '}', '}]'
    Tato metoda je odstraňuje, aby nedošlo k uložení do databáze

    :param tags_input_value: Vstupní data
    :return: Očištěná data
    '''
    formatted_tags = []
    for value in tags_input_value:
        if value not in [':', '[{', 'value', '{', '}', '}]']:
            formatted_tags.append(value)
    return formatted_tags