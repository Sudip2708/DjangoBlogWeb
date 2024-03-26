print("### main/users/views/user_sidebar_movements.py")

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def user_sidebar_movements(request, hash):

    # Ověření, zda je uživatel přihlášený
    if request.user.is_authenticated:

        # Získání přihlášeného uživatele
        user = request.user

        hash_to_process_values = (
            "#sidebar",
            "#sidebar_category_navigation",
            "#show_tab_for_similar",
            "#sidebar_category_menu",
            "#sidebar_user_user_menu",
            "#sidebar_user_author_menu",
            "#sidebar_search_options"
        )

        # Pokud se jedná o změnu viditelnosti sidebaru
        if hash in hash_to_process_values:
            user.change_sidebar_value(hash[1:])

        # Pokud se jedná o posun jednotlivých sidebarů
        else:
            user.sidebar_move(hash)

    # Získání odkazu na předchozí stránku
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Přesměrování zpět na předchozí stránku
    return HttpResponseRedirect(previous_page)

