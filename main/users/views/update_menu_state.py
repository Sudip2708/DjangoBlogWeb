from django.http import JsonResponse

def update_menu_state(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Ověření, zda je uživatel přihlášený
        if request.user.is_authenticated:

            # Získání přihlášeného uživatele
            user = request.user

            # Získání unikátního identifikátoru nabídky z AJAX požadavku
            menu_id = request.POST.get('menu_id')

            # Změna hodnoty pole sidebar_user_user_menu na opačnou
            if menu_id == "#userOptionsCollapse":
                user.sidebar_user_user_menu = not user.sidebar_user_user_menu
                user.save()

            # Změna hodnoty pole sidebar_user_user_menu na opačnou
            elif menu_id == "#authorOptionsCollapse":
                user.sidebar_user_author_menu = not user.sidebar_user_author_menu
                user.save()

        # Vrácení odpovědi na AJAX požadavek
        return JsonResponse({})

