def setting_values_check(dictionary, default_values):
    '''
    Funkce pro kontrolu položek slovníku dle defaultních hodnot.

    Funkce slouží k tomu, aby se dal aktualizovat seznam hodnot nastavení,
    dle seznamu defaultních hodnot (zejména při jejich rozšíření).
    Funkce obdrží slovník, který má být zkontrolován a slovník s defaultním nastavením.
    Funkce následně projde všechny položky slovníku s defaultním nastavením
    a kontroluje, zda kontrolovaný slovník obsahuje všechny klíče,
    které jsou obsaženy v defaultních hodnotách.

    Pokud některý klíč chybí nebo nemá vyplněnou hodnotu,
    bude přidán (nebo aktualizován) s defaultní hodnotou.

    Funkce vrací zkontrolovaný nebo aktualizovaný slovník.
    '''

    for key, value in default_values.items():
        dictionary.setdefault(key, value)
    return dictionary
