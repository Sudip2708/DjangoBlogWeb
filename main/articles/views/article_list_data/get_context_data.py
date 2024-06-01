def get_context_data(self, context, **kwargs):
    '''
    Metoda pro přidání obsahu potřebného k vykreslení stránky.

    Metoda je určená pro tyto URL:
    - article-list: Stránka zobrazující všechny publikované články.
    - article-category-list: Stránka zobrazující všechny publikované články roztříděné do kategorií.
    - article-tag-list: Stránka pro zobrazení článků pro daný tag.
    - article-tag-list-similar: Stránka pro zobrazení podobných článků pro daný tag.
    - article-tag-list-category: Stránka pro zobrazení kategorií pro články pro daný tag.
    - article-tag-list-similar-category: Stránka pro zobrazení kategorií pro podobné články pro daný tag.

    Metoda dědí z třídy BaseView následující obsah:
    - context['user']: Instance uživatele.
    - context['url_name']: URL jménu adresy z které požadavek přišel.
    - context['sidebar_search_form']: Formulář pro hledání (pro postranní panel).
    - context['published_categories']: Publikované kategorie (pro dropdown menu a postranní panel).
    - context['footer']: Data pro vykreslení patičky (na domácí stránce je již zahrnuto)
    - context['user_thumbnail']: Miniatura profilového obrázku (pro přihlášeného a nepřihlášeného uživatele).

    Metoda přidává kombinace těchto obsahů:
    - context['page_title']: Nadpis stránky.
    - context['mobile_page_title']: Nadpis stránky pro mobilní zařízení (jen pro všechny články a kategorie).
    - context['page_subtitle']: Podnadpis (pokud nejsou zobrazeny kategorie).
    - context['info_text']: Informační text o případném nenalezení žádného výsledu (pro podobné články).
    - context['current_category']: Instance aktuálně vybrané kategorie.
    - context['category_tabs']: Instance kategorií pro daný obsah.
    - context['current_tag']: Instance aktuálně vybraného tagu.
    '''

    # Kontex pro všechny stránky
    context['page_title'] = self.page_title

    # Kontex pro stránku se všemi články
    if self.url_name == 'article-list':
        context['page_title_mobile'] = self.page_title_mobile
        if self.user.settings.get('show_category_navigation'):
            context['current_category'] = self.current_category
            context['category_tabs'] = self.category_tabs
        else:
            context['page_subtitle'] = self.page_subtitle

    # Kontex pro stránku s kategoriemi
    elif self.url_name == 'article-category-list':
        context['page_title_mobile'] = self.page_title_mobile
        context['current_category'] = self.current_category
        if self.user.settings.get('show_category_navigation'):
            context['category_tabs'] = self.category_tabs
        else:
            context['page_subtitle'] = self.page_subtitle

    # Pokud jsme na stránce s podobnýmy články na základě tagu
    elif self.url_name.startswith('article-tag'):
        context['current_tag'] = self.current_tag
        if not self.article_ids:
            context['info_text'] = self.info_text
        if not self.user.settings.get('show_tab_for_similar'):
            context['page_subtitle'] = self.page_subtitle
        if self.url_name.endswith('category'):
            context['current_category'] = self.current_category
            context['category_tabs'] = self.category_tabs

    return context
