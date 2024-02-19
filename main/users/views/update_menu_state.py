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
            if menu_id == "#sidebarCollapse":
                user.sidebar = not user.sidebar
                user.save()
                return JsonResponse({'reload_page': True})

            # Změna hodnoty pole sidebar_user na opačnou
            elif menu_id == "#userCollapse":
                user.sidebar_user = not user.sidebar_user
                user.save()

            # Změna hodnoty pole sidebar_user_user_menu na opačnou
            elif menu_id == "#userOptionsCollapse":
                user.sidebar_user_user_menu = not user.sidebar_user_user_menu
                user.save()

            # Změna hodnoty pole sidebar_user_author_menu na opačnou
            elif menu_id == "#authorOptionsCollapse":
                user.sidebar_user_author_menu = not user.sidebar_user_author_menu
                user.save()

            # Změna hodnoty pole sidebar_search na opačnou
            elif menu_id == "#searchCollapse":
                user.sidebar_search = not user.sidebar_search
                user.save()

            # Změna hodnoty pole sidebar_category na opačnou
            elif menu_id == "#categoryCollapse":
                user.sidebar_category = not user.sidebar_category
                user.save()

            # Změna hodnoty pole sidebar_tags na opačnou
            elif menu_id == "#tagsCollapse":
                user.sidebar_tags = not user.sidebar_tags
                user.save()


        # Vrácení odpovědi na AJAX požadavek
        return JsonResponse({})

