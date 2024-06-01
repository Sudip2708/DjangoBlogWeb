from django.http import JsonResponse

def user_sidebar_appearance(request):
    '''
    Pohled pro změnu boolean hodnot v databázi pro nastavení bočního panelu.

    Pohled přijímá požadavek obdržený prostřednictvím AJAX ze scriptu stránky.

    Pohled nejprve kontroluje, zdali se jedná o POST a zda je HTTP požadavek odeslán pomocí JavaScriptu
    jako AJAX požadavek (hlavička obsahuje hodnotu XMLHttpRequest).

    Pohled po té z požadavku získá hodnotu 'menu_id' z které následně odebere počáteční hash
    a získá tak název klíče slovníku, pro který má být hodnota měněna.

    Následně pohled s tímto klíčem volá metodu 'change_sidebar_bool_value' uživatele,
    která změní hodnotu daného klíče na jeho opak (True/False),
    a po úspěšném vykonání navrací prázdný slovník.
    '''

    # Ověření, zda se jedná o POST požadavek zaslaný prostřednictvím AJAX
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':

        # Získání klíče, pro který má být měněna hodnota
        menu_id = request.POST.get('menu_id')
        field_id = menu_id[1:]

        # Volání metody pro změnu hodnoty a návrat prázdného slovníku
        request.user.change_sidebar_bool_value(field_id)
        return JsonResponse({})
