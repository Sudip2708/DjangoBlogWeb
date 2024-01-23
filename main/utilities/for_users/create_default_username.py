# Metoda volaná z main/users/models.py


def create_default_username(slugify_email, CustomUser):
    '''
    Vytvoření uživatelského jména na základě slagifikovaného emailu.

    :param slugify_email: Slagifikovaný email uživatele
    :param CustomUser: Instance uživatele
    :return: Nové jméno uživatele, v případě schody s jiným uživatelem, dochází k číslování.
    '''

    # Definice proměnných
    new_username = username = slugify_email
    counter = 1

    # Kontrola jedinečnosti username a případné přidání číselné hodnoty
    while CustomUser.objects.filter(username=new_username).exists():
        counter += 1
        new_username = f"{username}_{counter}"

    return new_username