from django.http import HttpResponseRedirect

def user_sidebar_movements(request, hash):
    '''
    Pohled pro změnu pořadí bočních panelů.

    Pohled nejprve ověří, zda požadavek obsahuje 'hash' s požadavkem na změnu pozice bočního panelu,
    a pokud ano, volá metodu pro změnu jeho pořadí.

    Následně se provede načtení předchozí stránky a návratu na ni.
    '''

    # Ověření, zda se jedná o posun panelů a volání příslušné metody
    if hash.startswith('#Move'):
        request.user.change_sidebar_order_value(hash)

    # Získání odkazu na předchozí stránku a přesměrování na ni
    previous_page = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_page)
