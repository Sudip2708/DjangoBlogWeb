from whoosh.index import open_dir
from django.conf import settings


def update_field_in_index(self, article_id, field_name, new_value):
    '''
    Method of the ArticleSchema class for updating a specific field in the index.

    The method expects the following data:
    article_id = ID of the article for which the update is to be performed.
    field_name = Name of the field to be updated.
    new_value = New data for this field.

    First, the method opens the index file and then loads the methods for writing (writer).
    Then it updates the data for the specified field and article, and saves the changes.
    '''

    # Open the index file for writing.
    ix = open_dir(settings.INDEX_DIRECTORY)
    writer = ix.writer()

    # Update the data and save the changes.
    writer.update_document(id=str(article_id), **{field_name: new_value})
    writer.commit()
