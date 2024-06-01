from django.utils import timezone

from ...schema.article_schema import ArticleSchema


def handle_status_pre_save(article):
    '''
    Handler pro zachycení signálu pre_save pro změnu statusu článku.

    Handler ověřuje, zda instance článku již existuje (není to nový objekt).
    Pokud existuje, načte se stará instance článku na základě primárního klíče (pk)
    a uloží se původní status do atributu `previous_status`.

    Pokud je instance nový objekt, atribut `previous_status` se nastaví na None.
    '''

    # Zkontrolujte, zda instance již existuje (není to nový objekt)
    if article.pk:
        article_class = article._meta.model
        old_instance = article_class.objects.get(pk=article.pk)
        article.previous_status = old_instance.status
    else:
        article.previous_status = None


async def handle_status_post_save(article):
    '''
    Asynchronní handler pro zachycení post_save signálu pro změnu statusu článku.

    Handler ověřuje, zda již byl tento kód proveden (kontrola atributu `_status_save_done`).
    Pokud ne, zkontroluje, zda se status článku změnil.

    Pokud se status změnil a nový status je 'publish', článek se zaindexuje pomocí `ArticleSchema`,
    a pokud není nastavený datum publikování, nastaví se na aktuální datum a čas.
    A pokud se status změnil a původní status byl 'publish', článek se odstraní z indexu Whoosh.

    Nakonec se nastaví atribut `_status_save_done` na True, aby se zabránilo opakovanému
    spuštění tohoto kódu, a instance se uloží.
    '''

    # Kontrola, zda již byl tento kod proveden
    if not hasattr(article, '_status_save_done'):

        if article.previous_status != article.status:

            if article.status == 'publish':
                ArticleSchema().index_article(article)
                if not article.published:
                    article.published = timezone.now()

            elif article.previous_status == 'publish':
                ArticleSchema().delete_article_from_index(article.id)

            # Nastavení '_status_save_done' pro kontrolu, zda již byl tento kod proveden
            article._status_save_done = True
            article.save()
