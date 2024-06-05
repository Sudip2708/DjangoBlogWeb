import os
from whoosh.index import create_in, open_dir
from django.conf import settings
from whoosh.fields import SchemaClass, TEXT, DATETIME, ID

from .data.print_indexed_articles import print_indexed_articles
from .data.index_article import index_article
from .data.delete_article_from_index import delete_article_from_index
from .data.update_field_in_index import update_field_in_index


class ArticleSchema:
    '''
    The ArticleSchema class defines the schema for indexing articles using Whoosh.

    The class allows for the initialization and management of a Whoosh index for article indexing.
    It includes a method for creating the index and defines the schema
    used to index individual article attributes, including: title, overview, content, author, and publication date.

    The schema is used for more efficient full-text searching in published articles.
    Functions related to search handling are thus linked to the schema.
    The class also includes the rebuild_schema function located in the data module,
    which is used to reindex the entire schema.

    This class contains the following methods:
    - update_field_in_index: For updating a specific field in the index.
    - delete_article_from_index: For deleting an article from the index.
    - index_article: For indexing an article.
    - print_indexed_articles: For printing the titles of all indexed articles.
    '''

    def __init__(self):
        ''' Class initialization method. '''
        self.ix = self.create_index()

    def create_index(self):
        '''
        The method opens, creates, or returns an open index from its location.

        The create_index method creates or opens a Whoosh index
        in the directory specified by the settings.INDEX_DIRECTORY variable.
        If the directory does not exist yet, the method creates it.
        It then checks if the directory is empty.
        If it is, it creates a new index using the schema obtained via the get_schema method.
        If the directory already contains some files,
        the method simply opens the existing index in that directory.

        Finally, it returns the open index.
        '''

        # Check/create directory
        if not os.path.exists(settings.INDEX_DIRECTORY):
            os.makedirs(settings.INDEX_DIRECTORY)

        # Load and return index
        if not os.listdir(settings.INDEX_DIRECTORY):
            ix = create_in(settings.INDEX_DIRECTORY, self.get_schema())
        else:
            ix = open_dir(settings.INDEX_DIRECTORY)

        return ix

    def get_schema(self):
        '''
        The method defines the fields of the schema instance.

        The method returns an instance of the SchemaClass,
        which contains field definitions for indexing articles.
        '''

        return SchemaClass(
            id=ID(stored=True, unique=True),
            title=TEXT(stored=True),
            overview=TEXT(stored=True),
            content=TEXT(stored=True),
            author=ID(stored=True),
            published=DATETIME(stored=True),
        )

    def update_field_in_index(self, article_id, field_name, new_value):
        ''' Method for updating a specific field in the index. '''
        update_field_in_index(self, article_id, field_name, new_value)

    def delete_article_from_index(self, article_id):
        ''' Method for deleting an article from the index. '''
        delete_article_from_index(self, article_id)

    def index_article(self, article):
        ''' Method for indexing an article. '''
        index_article(self, article)

    def print_indexed_articles(self):
        ''' Method for printing the titles of all indexed articles. '''
        print_indexed_articles(self)
