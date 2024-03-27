print("### main/users/views/user_sidebar_movements.py")

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def user_sidebar_movements(request, hash):

    # Ověření, zda je uživatel přihlášený
    if request.user.is_authenticated:

        # Získání přihlášeného uživatele
        user = request.user

        # Pokud se jedná o posun jednotlivých sidebarů
        if hash.startswith('#Move'):
            user.sidebar_move(hash)

        # Pokud se jedná o změnu viditelnosti sidebaru
        else:
            user.change_sidebar_value(hash[1:])

    # Získání odkazu na předchozí stránku
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Odstranění '/similar/' a všeho za ním z URL
    if '/similar/' in previous_page:
        previous_page = previous_page.split('/similar/')[0]


    # Odstranění '/category/' a všeho za ním z URL
    elif '/category/' in previous_page:
        previous_page = previous_page.split('/category/')[0]

    # Přesměrování zpět na předchozí stránku
    return HttpResponseRedirect(previous_page)

