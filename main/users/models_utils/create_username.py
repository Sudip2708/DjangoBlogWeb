
def create_username(email, CustomUser):
    '''
    Funkce na vytvoření uživatelského jména na základě uživatelského emailu

    :param email: Email uživatele
    :param CustomUser: Instance uživatele

    :return: Nové jméno uživatele, v případě schody s jiným uživatelem, dochází k číslování.
    '''

    # Vytvoření základu pro uživatelské jméno: Přední část emailu (před @) + převést velká písmena na malá
    username = email.split('@')[0].lower()

    # Přidání pořadového čísla v případě, že uživatelské jméno již existuje
    counter = 1
    new_username = username

    while CustomUser.objects.filter(username=new_username).exists():
        counter += 1
        new_username = f"{username}_{counter}"

    return new_username