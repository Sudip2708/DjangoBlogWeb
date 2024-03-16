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

            # Odstranění hashe
            field_id = menu_id[1:]

            # Volání metody pro změnu hodnoty v mixinu
            user.change_sidebar_value(field_id)

        # Vrácení odpovědi na AJAX požadavek
        return JsonResponse({})
