from ....models.article import Article
from ...common_data.get_similar_data import get_similar_data
from ...common_data.get_category_data import get_category_data
from .get_tag_data import get_tag_data


def get_queryset_for_tags(self):
    '''
    Metoda pro vytvoření seznamu článků pro konkrétní tag a pro podobné články.

    Metoda je určená pro tyto URL:
    - article-tag-list: Stránka pro zobrazení článků pro daný tag.
    - article-tag-list-similar: Stránka pro zobrazení podobných článků pro daný tag.
    - article-tag-list-category: Stránka pro zobrazení kategorií pro články pro daný tag.
    - article-tag-list-similar-category: Stránka pro zobrazení kategorií pro podobné články pro daný tag.

    Atributy přidané nebo měněné touto metodou:
    - self.page_title: Název stránky.
    - self.page_subtitle: Podnázev stránky (zobrazí se, když je navigace pro kategorie skrytá).
    - self.info_text: Informační text (zobrazí se, když není nalezen žádný podobný článek).
    - self.current_category: Instance aktuálně vybrané kategorie (pouze pro kategorie).
    - self.category_tabs = Seznam kategorií pro obsah self.article_ids (pouze pro kategorie).

    Metoda nejprve volá metodu get_tag_data(self), která z adresy získá slug pro vybraný tag,
    a následně vytvoří hodnoty pro atributy:
    self.current_tag, self.article_ids, self.page_title a self.page_subtitle.

    Po té metoda ověří, zda požadavek přišel z adresy pro zobrazení podobných článků.
    Pokud ano volá metodu get_similar_data(self), která získá seznam podobných článků,
    které mají shodný alespoň jeden tag a nejsou obsaženy v původním seznamu.
    a následně vytvoří hodnoty pro atributy self.article_ids, self.page_title.
    Nakonec metoda ještě zkontroluje, zda nově vytvořený obsah pro self.article_ids
    obsahuje alespoň jeden záznam, a pokud ne, pak vytvoří obsah pro atribut self.info_text.

    Po té metoda ověří, zda požadavek přišel ze stránky, zobrazující navigaci pro kategorie.
    Pokud ano volá metodu get_category_data(self), která na základě aktuálně vybrané kategorie,
    vytvoří hodnoty pro atributy:
    self.article_ids, self.current_category, self.category_tabs a self.page_title.

    Nakonec metoda načte instance pro vybrané články a vrátí je jako queryset.
    '''

    # Nastavení pro stránku s tagy (article-tag-list)
    get_tag_data(self)

    # Nastavení pro stránku s podobnými články (article-tag-list-similar)
    if self.url_name.startswith('article-tag-list-similar'):
        get_similar_data(self)
        self.page_title = f'Similar Articles for Tag: {self.current_tag.name}'
        if not self.article_ids:
            self.info_text = 'There are no other articles with tags that have articles in the result.'

    # Nastavení pro se zobrazenými kategoriemi (article-tag-list-category, article-tag-list-similar-category)
    if self.url_name.endswith('category'):
        get_category_data(self)

    # Vytvoření a navrácení seznamu instancí článků
    queryset = Article.objects.filter(id__in=self.article_ids)
    return queryset
