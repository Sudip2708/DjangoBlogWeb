def change_sidebar_order(dictionary, hash):
    '''
    Funkce pro změnu pořadí postranních panelů.

    Funkce obdrží slovník s názvy postranních panelů a jako klíče jejich pořadí,
    a hash, který obsahuje informaci o směru pohybu (#MoveUp/#MoveDn)
    a informaci s jakým panelem je posouváno (7. znak je podtržítko,
    takže 8 znak a dál je název klíče panelu ve slovníku).

    Funkce nejprve vygeneruje ze získaného hashe tyto dvě hodnoty.
    A následně získává hodnotu pozice aktuálně posouvaného bočního panelu.
    Po té, za pomoci proměnné pro směr pohybu vypočítá novou hodnotu pořadí (+1/-1),
    a po té projde jednotlivé hodnoty slovníku a vrátí klíč k hodnotě, která odpovídá nové hodnotě umístění.

    Funkce nakonec prohodí mezi sebou hodnoty u těchto dvou slovníků,
    a vrací upravený slovník.
    '''

    try:

        # Načtení proměných z obdrženého hashe
        move = hash[:7]
        actual_sidebar = hash[8:]

        # Získání druhého sidebaru (s kterým se bude prohazovat pozice)
        actual_position = dictionary[actual_sidebar]
        new_position = actual_position + (-1 if move == '#MoveUp' else +1)
        next_sidebar = next(key for key, value in dictionary.items() if value == new_position)

        # Prohození hodnot pořadí a navrácení slovníku
        dictionary[actual_sidebar], dictionary[next_sidebar] = (
            dictionary[next_sidebar], dictionary[actual_sidebar]
        )
        return dictionary

    except Exception as e:
        print(f"###ERROR### change_sidebar_order_value: {e}")
