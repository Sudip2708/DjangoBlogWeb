from django.utils import timezone

from ...schema.article_schema import ArticleSchema


def handle_status_pre_save(article):
    '''
    Handler for capturing the pre_save signal for changing the article status.

    The handler checks if the article instance already exists (it's not a new object).
    If it exists, the old instance of the article is loaded based on the primary key (pk),
    and the original status is saved to the `previous_status` attribute.

    If the instance is a new object, the `previous_status` attribute is set to None.
    '''

    # Check if the instance already exists (it's not a new object)
    if article.pk:
        article_class = article._meta.model
        old_instance = article_class.objects.get(pk=article.pk)
        article.previous_status = old_instance.status
    else:
        article.previous_status = None


def handle_status_post_save(article):
    '''
    Handler for capturing the post_save signal for changing the article status.

    The handler checks if this code has already been executed (checking the `_status_save_done` attribute).
    If not, it checks if the article status has changed.

    If the status has changed and the new status is 'publish', the article is indexed using `ArticleSchema`,
    and if the publication date is not set, it is set to the current date and time.
    If the status has changed and the previous status was 'publish', the article is removed from the Whoosh index.

    Finally, the `_status_save_done` attribute is set to True to prevent repeated
    execution of this code, and the instance is saved.
    '''

    # Check if this code has already been executed
    if not hasattr(article, '_status_save_done'):

        if article.previous_status != article.status:

            if article.status == 'publish':
                ArticleSchema().index_article(article)
                if not article.published:
                    article.published = timezone.now()

            elif article.previous_status == 'publish':
                ArticleSchema().delete_article_from_index(article.id)

            # Set '_status_save_done' to control if this code has already been executed
            article._status_save_done = True
            article.save()
