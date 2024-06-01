def get_context_data(self, context, **kwargs):
    '''
    Metoda pro přidání obsahu potřebného k vykreslení stránky.

    Metoda je určená pro tyto URL:
    - article-search: Základní adresa sloužící k zadání a vyhodnocení parametrů hledání.
    - article-search-results: Stránka pro zobrazení výsledků vyhledávání.
    - article-search-similar: Stránka pro zobrazení podobných článků pro články z výsledku vyhledávání.
    - article-search-results-category: Stránka pro zobrazení kategorií pro výsledek vyhledávání.
    - article-search-similar-category: Stránka pro zobrazení kategorií pro podobné články.

    Metoda dědí z třídy BaseView následující obsah:
    - context['user']: Instance uživatele.
    - context['url_name']: URL jménu adresy z které požadavek přišel.
    - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
    - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
    - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
    - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

    Metoda přidává následující kombinace těchto obsahů:
    - context['query']: Slovník s parametry hledání.
    - context['page_title']: Nadpis stránky.
    - context['page_title_mobile']: Nadpis stránky pro mobilní zařízení.
    - context['display_text']: Popis vyhledávání.
    - context['info_text']: Informační text o případném nenalezení žádného výsledku (pro podobné články).
    - context['current_category']: Instance aktuálně vybrané kategorie.
    - context['category_tabs']: Instance kategorií pro daný obsah.
    '''

    if self.url_name == 'article-search-error':
        return context

    # Kontext pro všechny stránky
    context['query'] = self.search_parameters
    context['page_title'] = self.page_title
    context['page_title_mobile'] = self.page_title_mobile
    context['display_text'] = self.display_text

    # Kontext pro stránku s podobnými články
    if not self.article_ids:
        context['info_text'] = self.info_text

    # Kontext pro stránku s kategoriemi
    if self.url_name.endswith('category'):
        context['category_tabs'] = self.category_tabs
        context['current_category'] = self.current_category

    # Navrácení kontextu
    return context
