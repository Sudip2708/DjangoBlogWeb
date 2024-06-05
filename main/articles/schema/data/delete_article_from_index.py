from whoosh.index import open_dir
from django.conf import settings


def delete_article_from_index(self, article_id):
    '''
    Method of the ArticleSchema class for deleting an article from the index.

    This method is used to remove an article from the index,
    for example, when the article changes its status and is no longer public.

    The method expects an article instance.
    First, it opens the index file and then loads the methods for writing.
    Then, the method removes the entries from the index and saves the changes.
    '''

    # Open the index file for writing.
    ix = open_dir(settings.INDEX_DIRECTORY)
    writer = ix.writer()

    # Remove the document from the index and save the changes.
    writer.delete_by_term('id', str(article_id))
    writer.commit()
