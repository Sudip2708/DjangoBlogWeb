from django.utils.text import slugify

from common_data.get_unique_value import get_unique_value


def handle_default_values_pre_save(user):
    '''
    Handler pro zachycení signálu pre_save pro kontrolu výchozích hodnot.

    Nejprve handler zkontroluje, zda pole pro uživatelské jméno není prázdné.
    Pokud ano, vytvoří nové uživatelské jméno na základě přední části emailu
    a funkce pro vytvoření jedinečné hodnoty v rámci pole modelu 'get_unique_value'.

    Poté handler zkontroluje, zda hodnota pole 'slug' odpovídá hodnotě pole 'username'.
    Pokud ne, aktualizuje toto pole správnou hodnotou.
    '''

    # Vytvoření jedinečného uživatelského jména
    if not user.username:
        user_class = user._meta.model
        field = 'username'
        value = slugify(user.email.split('@')[0])
        user.username = get_unique_value(user_class, field, value)

    # Kontrola, zda slug odpovídá aktuálnímu uživatelskému jménu
    if user.slug != slugify(user.username):
        user.slug = slugify(user.username)
