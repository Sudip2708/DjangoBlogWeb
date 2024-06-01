from ...models.article import Article
from ...models.article_author import ArticleAuthor


def get_queryset(self):
    '''
    Metoda slouží k získání článků zobrazených na stránce.

    Metoda je určená pro tyto URL:
    - my-articles: Stránka pro články od autora navázaného na uživatele.

    Stránka má následující záložky:
    - all: Všechny články řazené dle data vytvoření sestupně.
    - drafted: Rozepsané články.
    - publish: Publikované články (články pro veřejnost).
    - archive: Archivované články.

    Atributy přidané nebo měněné touto metodou:
    - self.page_title: Název stránky.
    - self.page_title_mobile: Atribut pro nadpis stránky pro mobilní zařízení.
    - self.current_tab: Atribut pro název aktuálně zobrazené záložky.

    Metoda v tomto kodu zjistí z jaké záložky požadavek přišel
    a následně vytváří obsah pro zobrazení článků dané záložky.

    Metoda vrací instance článků určených k zobrazení na stránce.
    '''

    # Načtení aktuální záložky z adresy stránky
    self.current_tab = self.kwargs.get('current_tab')

    # Načtení autora
    author = ArticleAuthor.objects.get(id=self.user.linked_author.id)

    # Načtení článků pro záložku Drafted
    if self.current_tab == 'drafted':
        queryset = Article.objects.filter(author=author, status='drafted') \
                                  .order_by('-created')

    # Načtení článků pro záložku Publish
    elif self.current_tab == 'publish':
        queryset = Article.objects.filter(author=author, status='publish') \
                                  .order_by('-created')

    # Načtení článků pro záložku Archiv
    elif self.current_tab == 'archive':
        queryset = Article.objects.filter(author=author, status='archive') \
                                  .order_by('-created')

    # Načtení článků pro záložku All
    else:
        queryset = Article.objects.filter(author=author) \
                                  .order_by('-created')

    return queryset
