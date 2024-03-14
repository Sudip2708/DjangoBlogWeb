print("### main/users/views/user_sidebar_movements.py")

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def user_sidebar_movements(request, hash):

    # Ověření, zda je uživatel přihlášený
    if request.user.is_authenticated:

        # Získání přihlášeného uživatele
        user = request.user

        # Změna hodnoty pole sidebar_user_user_menu na opačnou
        if hash == "#sidebarCollapse":
            user.sidebar = not user.sidebar
            user.save()

        # Posunu sidebaru nahoru
        elif hash == "#userMoveUp":
            user.sidebar_move_up(hash)

        # Posunu sidebaru dolu
        elif hash == "#userMoveDown":
            user.sidebar_move_down(hash)

        # Posunu sidebaru nahoru
        elif hash == "#searchMoveUp":
            user.sidebar_move_up(hash)

        # Posunu sidebaru dolu
        elif hash == "#searchMoveDown":
            user.sidebar_move_down(hash)

        # Posunu sidebaru nahoru
        elif hash == "#categoryMoveUp":
            user.sidebar_move_up(hash)

        # Posunu sidebaru dolu
        elif hash == "#categoryMoveDown":
            user.sidebar_move_down(hash)

        # Posunu sidebaru nahoru
        elif hash == "#tagsMoveUp":
            user.sidebar_move_up(hash)

        # Posunu sidebaru dolu
        elif hash == "#tagsMoveDown":
            user.sidebar_move_down(hash)

    # Získání odkazu na předchozí stránku
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Přesměrování zpět na předchozí stránku
    return HttpResponseRedirect(previous_page)

