from django.utils.text import slugify

from common_data.get_unique_value import get_unique_value

from ...models.article_category import ArticleCategory


def handle_default_values_pre_save(article):
    '''
    Handler pro zachycení signálu pre_save pro kontrolu výchozích hodnot.

    Handler kontroluje, zda se jedná o vytvoření nové instance (instance ještě nemá přidělené ID).
    Pokud ano, zkontroluje, zda je vyplněna kategorie článku.
    Pokud není, přidá článku kategorii 'Uncategorized' (kategorie s ID 1 v modelu ArticleCategory).
    Dále pak kontroluje, zda je vyplněn status článku.
    Pokud není, přidá článku status 'drafted' (který slouží pro vytváření článků).

    Následně handler zkontroluje, zda článek obsahuje nadpis.
    Pokud ne, volá funkci 'get_unique_value' pro vytvoření jedinečného názvu.

    A poté handler zkontroluje, zda hodnota pole 'slug' odpovídá hodnotě pole 'title' pro nadpis článku.
    Pokud ne, aktualizuje toto pole správnou hodnotou.
    '''
    # Kontrola, zda se jedná o vytvoření instance
    if not article.id:

        # Vytvoření kategorie, pokud není
        if not article.category:
            article.category = ArticleCategory.objects.get(id=1)

        # Vytvoření statusu, pokud není
        if not article.status:
            article.status = 'drafted'

    # Vytvoření jedinečného jména článku
    if not article.title:
        model = article._meta.model
        field = 'title'
        value = f'Článek {article.id}'
        article.title = get_unique_value(model, field, value)

    # Kontrola, zda slug odpovídá aktuální hodnotě názvu článku
    if article.slug != slugify(article.title):
        article.slug = slugify(article.title)
