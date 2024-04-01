print("### main/users/views/user_sidebar_appearance.py")

from django.http import JsonResponse


def user_sidebar_appearance(request):
    '''
    Pohled pro manipulaci s vzhledem bočního panelu uživatele.

    Přijímá request, což je HttpRequest objekt reprezentující aktuální požadavek.
    Funkce provádí akci pouze v případě, že jde o POST požadavek a že požadavek pochází z AJAX.
    Poté získává unikátní identifikátor nabídky z AJAX požadavku,
    provádí změnu hodnoty vzhledu bočního panelu uživatele
    a vrací prázdnou odpověď na AJAX požadavek pomocí JsonResponse.

    :param request: HttpRequest objekt reprezentující aktuální požadavek.
    :return: JsonResponse objekt obsahující prázdnou odpověď na AJAX požadavek.
    '''

    # Jedná li se o POST požadavek
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Získání unikátního identifikátoru nabídky z AJAX požadavku
        menu_id = request.POST.get('menu_id')

        # Odstranění hashe
        field_id = menu_id[1:]

        # Volání metody pro změnu hodnoty v mixinu
        request.user.change_sidebar_value(field_id)

        # Vytiskne aktuální nastavení uživatele
        request.user.print_current_user_settings(request)

        # Vrácení prázdné odpovědi na AJAX požadavek
        return JsonResponse({})
