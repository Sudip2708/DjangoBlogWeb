from .get_queryset_data.get_queryset_for_articles import get_queryset_for_articles
from .get_queryset_data.get_queryset_for_categories import get_queryset_for_categories
from .get_queryset_data.get_queryset_for_tags import get_queryset_for_tags

def get_queryset(self, *args, **kwargs):
    '''
    Metoda slouží k získání článků zobrazených na stránce.

    Metoda je určená pro tyto URL:
    - article-list: Stránka zobrazující všechny publikované články.
    - article-category-list: Stránka zobrazující všechny publikované články roztříděné do kategorií.
    - article-tag-list: Stránka pro zobrazení článků pro daný tag.
    - article-tag-list-similar: Stránka pro zobrazení podobných článků pro daný tag.
    - article-tag-list-category: Stránka pro zobrazení kategorií pro články pro daný tag.
    - article-tag-list-similar-category: Stránka pro zobrazení kategorií pro podobné články pro daný tag.

    Atributy přidané nebo měněné touto metodou:
    - self.page_title: Název stránky.
    - self.page_title_mobile: Název stránky pro mobilní zařízení.
    - self.page_subtitle: Podnázev stránky (zobrazí se, když je navigace pro kategorie skrytá).
    - self.info_text: Informační text (zobrazí se, když není nalezen žádný podobný článek).
    - self.current_category: Instance aktuálně vybrané kategorie (pouze pro kategorie).
    - self.category_tabs = Seznam kategorií pro obsah self.article_ids (pouze pro kategorie).

    Metoda v tomto kodu zjistí z jaké adresy požadavek přišel
    a následně volá příslušnou metodu pro spracování požadavku.

    Metoda vrací instance článků určených k zobrazení na stránce.
    '''

    # Nastavení pro stránku zobrazující všechny články
    if self.url_name == 'article-list':
        queryset = get_queryset_for_articles(self)

    # Nastavení pro stránky zobrazující obsah pro určitou kategorii.
    elif self.url_name == 'article-category-list':
        queryset = get_queryset_for_categories(self)

    # Nastavení pro stránky zobrazující obsah pro určitý tag.
    elif self.url_name.startswith('article-tag'):
        queryset = get_queryset_for_tags(self)

    return queryset
