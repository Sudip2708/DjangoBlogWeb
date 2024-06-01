from django.utils.text import slugify

from common_data.get_unique_value import get_unique_value


def handle_default_values_pre_save(author):
    '''
    Handler pro zachycení signálu pre_save pro kontrolu výchozích hodnot.

    Nejprve handler zkontroluje, zda pole pro uživatelské jméno není prázdné.
    Pokud ano, vytvoří nové uživatelské jméno na základě přední části emailu
    a funkce pro vytvoření jedinečné hodnoty v rámci pole modelu 'get_unique_value'.

    Poté handler zkontroluje, zda hodnota pole 'slug' odpovídá hodnotě pole 'username'.
    Pokud ne, aktualizuje toto pole správnou hodnotou.
    '''

    # Vytvoření jedinečného uživatelského jména
    if not author.name:
        author_class = author._meta.model
        field = 'name'
        value = slugify(author.linked_user.username)
        author.name = get_unique_value(author_class, field, value)

    # Kontrola, zda slug odpovídá aktuálnímu uživatelskému jménu
    if author.slug != slugify(author.name):
        author.slug = slugify(author.name)

