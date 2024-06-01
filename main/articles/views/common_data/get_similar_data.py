from taggit.models import Tag

from ...models.article import Article


def get_similar_data(self):
    '''
    Metoda pro vytvoření atributů pro zobrazení podobných článků.

    Metoda je použita v těchto souborech:
    - articles/views/article_list_data/get_queryset_data/get_queryset_for_tags.py
    - articles/views/search_data/get_queryset.py

    Atributy přidané nebo měněné touto metodou:
    - self.article_ids: ID článků které obsahují vybraný tag.
    - self.info_text: Informační text (zobrazí se, když není nalezen žádný podobný článek).

    Metoda nejprve získá množinu ID tagů pro články obsažené v self.article_ids.

    Následně pro tuto množinu ID tagů vyhledá množinu ID článků,
    které obsahují alespoň jeden tag z množiny tagů,
    a zároveň nejsou součástí self.article_ids,
    a přepíše původní obsah self.article_ids těmito novými daty.
    '''

    # Získání ID tagů pro články z dotazu
    unique_tag_ids = Tag.objects \
                        .filter(article__id__in=self.article_ids) \
                        .values_list('id', flat=True) \
                        .distinct()

    # Získání ID článků, které obsahují alespoň jeden tag, nejsou součástí původního seznamu a mají status publish
    self.article_ids = Article.objects \
                                    .filter(status='publish', tags__id__in=unique_tag_ids) \
                                    .exclude(id__in=self.article_ids) \
                                    .values_list('id', flat=True) \
                                    .distinct()


