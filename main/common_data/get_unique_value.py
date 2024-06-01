def get_unique_value(model, field, value):
    '''
    Funkce pro ověření jedinečnosti dané hodnoty v rámci pole modelu.

    Funkce je použita v těchto souborech:
    - articles/signals/article_handlers/default_values_handler.py
    - articles/signals/article_author_handlers/default_values_handler.py
    - users/signals/user_handlers/default_values_handler.py

    Funkce očekává tyto tři parametry:
    - model: Instance modelu který bude použit pro kontrolu.
    - field: Pole modelu, kde bude kontrola probíhat.
    - value: Hodnota, která se v rámci pole a modelu bude ověřovat.

    Funkce nejprve ověří samotnou hodnotu, zda je jedinečná v rámci pole modelu.
    Pokud není, funkce přidá za hodnotu číslici 1 a ověří její jedinečnost.
    Takto pomocí while cyklu pokračuje dokud se nedostane na výraz,
    který v daném poli databáze neexistuje.

    Funkce vrací buď původní zadanou hodnotu (je-li jedinečná),
    nebo pozměněnou hodnotu s přidaným číslem.
    '''

    # Kontrola, zda zadaná hodnota existuje
    if model.objects.filter(**{field: value}).exists():

        suffix = 1
        new_value = f"{value}{suffix}"

        # Cyklus na dohledání jedinečné hodnoty
        while model.objects.filter(**{field: new_value}).exists():
            suffix += 1
            new_value = f"{value}{suffix}"

        value = new_value

    return value
