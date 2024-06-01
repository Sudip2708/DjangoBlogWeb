from django.shortcuts import get_object_or_404
from taggit.models import Tag

from ....models.article import Article


def get_tag_data(self):
    '''
    Metoda pro vytvoření seznamu článků pro konkrétní tag

    Atributy přidané nebo měněné touto metodou:
    - self.current_tag: Aktuálně vybraný tag.
    - self.article_ids: ID článků které obsahují vybraný tag.
    - self.page_title: Název stránky.
    - self.page_subtitle: Podnázev stránky (zobrazí se, když je navigace pro podobné články skrytá).

    Metoda nejprve načte z adresy slug aktuálně vybraného tagu,
    a následně získá jeho instanci a uloží ji jako atribut self.current_tag.
    (V případě, že nebude nalezena kategorie pro daný slug, vyvolá se výjimka 404.)

    Po té metoda načte množinu ID článků obsahující daný tag,
    a uloží ji jako atribut self.article_ids.

    Následně vytvoří atribut self.page_title pro název stránky,
    a pokud není zaplá navigace pro podobné články,
    vytvoří i atribut self.page_subtitle pro popisný text.
    '''

    # Získání aktuálně vybraného tagu
    current_tag_slug = self.kwargs.get('tag_slug')
    self.current_tag = get_object_or_404(Tag, slug=current_tag_slug)

    # Načtení ID článků pro daný tag
    self.article_ids = Article.objects \
                              .filter(tags=self.current_tag, status='publish') \
                              .values_list('id', flat=True)

    # Vytvoření nadpisu stránky
    self.page_title = f'Articles with Tag: {self.current_tag.name}'

    # Vytvoření podnadpisu stránky pokud není zapnutá navigace pro podobné články
    if not self.user.settings.get('show_tab_for_similar'):
        self.page_subtitle = 'To see tab for similar articles click on Show Similar in navbar.'
