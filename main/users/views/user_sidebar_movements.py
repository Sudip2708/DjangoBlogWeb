print("### main/users/views/user_sidebar_movements.py")

from django.http import HttpResponseRedirect

def user_sidebar_movements(request, hash):
    '''
    Pohled pro manipulaci s bočním panelem uživatele.

    Argumenty request a hash jsou přijímány,
    kde request je HttpRequest objekt reprezentující aktuální požadavek
    a hash je identifikátor akce, která se má provést.
    Pohled má nastarost spracování těchto požadavků:
    Posouvání bočních panelů v rámci jejich pořadí.
    Zobrazení a skrytí navigačních lišt pro kategorie a podobné články na základě tagů.
    Zobrazení a skrytí bočního panelu.
    Funkce pak provádí požadovanou akci a následně přesměrovává uživatele zpět na stránku.

    :param request: HttpRequest objekt reprezentující aktuální požadavek.
    :param hash: Hashování, které identifikuje, jaká akce se má provést s bočním panelem.
    :return: HttpResponse objekt přesměrovávající uživatele zpět na předchozí stránku.
    '''

    # Pokud se jedná o posun jednotlivých sidebarů
    if hash.startswith('#Move'):
        request.user.sidebar_move(hash)

    # Pokud se jedná o změnu viditelnosti sidebaru
    else:
        request.user.change_sidebar_value(hash[1:])

    # Získání odkazu na předchozí stránku
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Pokud jsme na stránce pro tagy (po odstranění navigace návrat na daný tag)
    if '/tag/' in previous_page:

        # Pokud jsme na záložce pro podobné články
        if '/similar/' in previous_page:
            # Odstranění '/similar/' a všeho za ním z URL
            previous_page = previous_page.split('/similar/')[0]


        # Pokud jsme na záložce pro kategorie
        elif '/category/' in previous_page:
            # Odstranění '/category/' a všeho za ním z URL
            previous_page = previous_page.split('/category/')[0]

    # Přesměrování zpět na předchozí stránku
    return HttpResponseRedirect(previous_page)

