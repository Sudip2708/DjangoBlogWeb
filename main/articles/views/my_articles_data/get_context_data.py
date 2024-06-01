def get_context_data(self, context, **kwargs):
    '''
    Metoda pro přidání obsahu potřebného k vykreslení stránky.

    Metoda je určená pro tyto URL:
    - my-articles: Stránka pro články od autora navázaného na uživatele.

    Metoda dědí z třídy BaseView následující obsah:
    - context['user']: Instance uživatele.
    - context['url_name']: URL jménu adresy z které požadavek přišel.
    - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
    - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
    - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
    - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

    Metoda vytváří a přidává tento obsah:
    - context['page_title']: Nadpis stránky.
    - context['mobile_page_title']: Nadpis stránky pro mobilní zařízení.
    - context['current_tab']: Název aktuálně zvolená záložka.
    '''

    context['page_title'] = 'My Articles'
    context['page_title_mobile'] = 'My Articles'
    context['current_tab'] = self.current_tab

    return context