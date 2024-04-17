print("### main/users/views/user_sidebar_appearance.py")

from django.http import JsonResponse


def user_sidebar_appearance(request):
    '''
    Pohled pro změnu hodnto v databázi při zobrazení a skrytí vyklápěcích nabídek bočního panelu.

    Přijímá request, což je HttpRequest objekt reprezentující aktuální požadavek.
    Funkce provádí akci pouze v případě, že jde o POST požadavek a že požadavek pochází z AJAX.
    Poté získává unikátní identifikátor (menu_id) nabídky z AJAX požadavku,
    provádí změnu hodnoty vzhledu bočního panelu v databázy
    a vrací prázdnou odpověď na AJAX požadavek pomocí JsonResponse.

    :param request: HttpRequest objekt reprezentující aktuální požadavek.
    :return: JsonResponse objekt obsahující prázdnou odpověď na AJAX požadavek.
    '''

    # Ověření, zda se jedná o POST požadavek
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print('### if request.method == POST and request.headers.get(X-Requested-With) == XMLHttpRequest:')

        # Získání unikátního identifikátoru nabídky z AJAX požadavku
        menu_id = request.POST.get('menu_id')
        print('### menu_id: ', menu_id)

        # Odstranění hashe
        field_id = menu_id[1:]

        # Volání metody pro změnu hodnoty v mixinu
        request.user.change_sidebar_value(field_id)

        # Vrácení prázdné odpovědi na AJAX požadavek
        return JsonResponse({})
