print("### main/users/views/user_sidebar_movements.py")

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def user_sidebar_movements(request, hash):

    # Ověření, zda je uživatel přihlášený
    if request.user.is_authenticated:

        # Získání přihlášeného uživatele
        user = request.user

        # Pokud se jedná o změnu viditelnosti sidebaru
        if hash == "#sidebarCollapse":
            user.change_sidebar_value('sidebar_appearance')
        # Pokud se jedná o posun jednotlivých sidebarů
        else:
            user.sidebar_move(hash)

    # Získání odkazu na předchozí stránku
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Přesměrování zpět na předchozí stránku
    return HttpResponseRedirect(previous_page)

