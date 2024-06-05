import os
import shutil
from whoosh.index import open_dir
from django.conf import settings

from ...models.article import Article


def rebuild_schema(self):
    '''
    Function for deleting and recreating the entire schema.

    First, the function checks if the schema folder exists (according to the location defined in settings.py).
    If the folder exists, the function first closes the index (in case it is open somewhere)
    and then deletes the entire folder using the shutil.rmtree() command.

    Then the function creates a new folder for the index and calls the method to create the index.

    Next, the function loads all articles from the Article model with the 'publish' status
    and writes each article to the index using a loop.
    '''

    # Load the schema
    from ...schema.article_schema import ArticleSchema

    # Delete the original folder (if it exists)
    if os.path.exists(settings.INDEX_DIRECTORY):
        ix = open_dir(settings.INDEX_DIRECTORY)
        ix.close()
        shutil.rmtree(settings.INDEX_DIRECTORY)

    # Create a new folder with the index
    os.makedirs(settings.INDEX_DIRECTORY)
    ArticleSchema().create_index()

    # Indexing articles
    articles = Article.objects.filter(status='publish')
    for article in articles:
        ArticleSchema().index_article(article)
