from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def user_sidebar_movements(request, hash):
    # Tiskne hash z URL adresy
    print("Hash value:", hash)

    # Ověření, zda je uživatel přihlášený
    if request.user.is_authenticated:
        print("### if request.user.is_authenticated:")

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


# def user_sidebar_movements(request):
#     if request.method == 'GET':
#         # Zpracování hodnoty hash z URL adresy
#         full_url = request.build_absolute_uri()
#         print("Full URL:", full_url)
#         referer_url = request.META.get('HTTP_REFERER', '/')
#         print("referer_url:", referer_url)
#
#         # # Ověření, zda je uživatel přihlášený
#         # if request.user.is_authenticated:
#         #     print("### if request.user.is_authenticated:")
#         #
#         #     # Získání přihlášeného uživatele
#         #     user = request.user
#         #
#         #     # Získání unikátního identifikátoru nabídky z AJAX požadavku
#         #     menu_id = request.POST.get('menu_id')
#         #     print("### menu_id: ", menu_id)
#         #
#         #     # Změna hodnoty pole sidebar_user_user_menu na opačnou
#         #     if menu_id == "#sidebarCollapse":
#         #         user.sidebar = not user.sidebar
#         #         user.save()
#         #
#         #     # Posunu sidebaru nahoru
#         #     elif menu_id == "#userMoveUp":
#         #         user.sidebar_move_up(menu_id)
#         #
#         #     # Posunu sidebaru dolu
#         #     elif menu_id == "#userMoveDown":
#         #         user.sidebar_move_down(menu_id)
#         #
#         #     # Posunu sidebaru nahoru
#         #     elif menu_id == "#searchMoveUp":
#         #         user.sidebar_move_up(menu_id)
#         #
#         #     # Posunu sidebaru dolu
#         #     elif menu_id == "#searchMoveDown":
#         #         user.sidebar_move_down(menu_id)
#         #
#         #     # Posunu sidebaru nahoru
#         #     elif menu_id == "#categoryMoveUp":
#         #         user.sidebar_move_up(menu_id)
#         #
#         #     # Posunu sidebaru dolu
#         #     elif menu_id == "#categoryMoveDown":
#         #         user.sidebar_move_down(menu_id)
#         #
#         #     # Posunu sidebaru nahoru
#         #     elif menu_id == "#tagsMoveUp":
#         #         user.sidebar_move_up(menu_id)
#         #
#         #     # Posunu sidebaru dolu
#         #     elif menu_id == "#tagsMoveDown":
#         #         user.sidebar_move_down(menu_id)
#
#
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))