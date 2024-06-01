from django.http import HttpResponseRedirect

def user_navigation_settings(request, hash):
    '''
    Pohled pro nastavení viditelnosti navigačních panelů a postranního panelu.

    Pohled zpracovává následující klíče slovníků:
    - show_sidebars: Viditelnost bočních panelů.
    - show_category_navigation: Viditelnost navigace pro kategorie.
    - show_tab_for_similar: Viditelnost pro navigaci pro podobné články.

    Pohled nejprve načítá adresu stránky ze kterého požadavek přišel.

    Pohled následně ověří, zda hodnota 'hash' začíná s '#bool' (položky pro změnu True/False),
    Pokud ano, vygeneruje z hashe část obsahující klíč pro nalezení položky ve slovníku.

    Poté ověří, zda jde o požadavek pro změnu viditelnosti bočního panelu,
    nebo pro změnu viditelnosti navigace pro kategorie,
    nebo pro změnu viditelnosti navigace pro podobné články,
    a volá příslušnou metodu pro provedení změny v databázi.

    Pokud se jedná o požadavek pro změnu viditelnosti navigace pro podobné články,
    pohled ověří, zda nejsme na záložce pro podobné články k danému tagu,
    pokud ano, odstraní tuto část z adresy.
    Pohled následně ověří, zda se nenacházíme na záložce kategorie,
    pokud ano, odstraní tuto část z adresy.

    Oba kroky mají za cíl zajistit, aby se při návratu na daný tag
    načetla při návratu stránka pro daný tag a ne pro určitou záložku
    pro kategorie článků daného tagu nebo podobné články k danému tagu.

    Pohled nakonec volá buď takto upravenou návratovou stránku pro daný tag,
    nebo se navrací na stránku, odkud požadavek přišel.
    '''

    # Získání odkazu na předchozí stránku
    previous_page = request.META.get('HTTP_REFERER', '/')

    # Ověření požadavku a přesměrování na příslušnou metodu
    if hash.startswith('#bool'):
        key = hash[6:]

        # Požadavek na změnu viditelnosti bočních panelů
        if key == 'show_sidebars':
            request.user.change_sidebar_bool_value(key)

        # Požadavek na změnu viditelnosti navigace pro kategorie
        elif key == 'show_category_navigation':
            request.user.change_settings_bool_value(key)

        # Požadavek na změnu viditelnosti navigace pro podobné články
        elif key == 'show_tab_for_similar':
            request.user.change_settings_bool_value(key)

            # Pokud jsme na záložce pro podobné články pro daný tag, návrat na stránku pro daný tag
            if '/similar/' in previous_page:
                previous_page = previous_page.split('/similar/')[0]

            # Pokud jsme na záložce pro kategorie pro daný tag, návrat na stránku pro daný tag
            elif '/category/' in previous_page:
                previous_page = previous_page.split('/category/')[0]

    return HttpResponseRedirect(previous_page)
