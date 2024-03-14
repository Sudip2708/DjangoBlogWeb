print("### main/users/views/user_sidebar_appearance.py")

from django.http import JsonResponse

def user_sidebar_appearance(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Ověření, zda je uživatel přihlášený
        if request.user.is_authenticated:

            # Získání přihlášeného uživatele
            user = request.user

            # Získání unikátního identifikátoru nabídky z AJAX požadavku
            menu_id = request.POST.get('menu_id')

            # Změna hodnoty pole sidebar_user na opačnou
            if menu_id == "#userCollapse":
                user.sidebar_user.value = not user.sidebar_user.value
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
                user.sidebar_search.value = not user.sidebar_search.value
                user.save()

            # Změna hodnoty pole sidebar_category na opačnou
            elif menu_id == "#categoryCollapse":
                user.sidebar_category.value = not user.sidebar_category.value
                user.save()

            # Změna hodnoty pole sidebar_tags na opačnou
            elif menu_id == "#tagsCollapse":
                user.sidebar_tags.value = not user.sidebar_tags.value
                user.save()

            # Změna hodnoty pole navigace pro kategorie
            elif menu_id == "#categoryNavigationCollapse":
                user.sidebar_category_navigation = not user.sidebar_category_navigation
                user.save()
                return JsonResponse({'reload_page': True})

            # Změna hodnoty pole sidebar_search_option na opačnou
            elif menu_id == "#searchOptionsCollapse":
                user.sidebar_search_options = not user.sidebar_search_options
                user.save()

        # Vrácení odpovědi na AJAX požadavek
        return JsonResponse({})
