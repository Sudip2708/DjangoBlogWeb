import os

from ...schema.article_schema import ArticleSchema
from .delete_unused_tags_handler import handle_delete_unused_tags_post_save


def handle_article_pre_delete(article):
    '''
    Handler to capture the pre_delete signal for deleting an article.

    The handler first verifies if the article has the status 'publish'.
    If it does, it means the article is indexed in Whoosh for faster full-text search,
    so in the next part of the code, it removes this record from the Whoosh index.

    The handler then creates an attribute '_picture_paths' containing an empty list
    and creates a list with fields for different sizes of the main article image.

    It then iterates through all these fields, and if they are not empty (which they shouldn't be),
    and if they do not contain a link to the default image (which they might),
    it adds the path to this image to the '_picture_paths' list.

    Furthermore, the handler fills the attribute 'tags_to_delete' with all the tags from the article
    (this list will be passed to the post_delete signal to check and potentially delete tags that are no longer used elsewhere).
    '''

    # Remove from Whoosh index (if the article is published)
    if article.status == 'publish':
        article_schema = ArticleSchema()
        article_schema.delete_article_from_index(article.id)

    # Create a list of image paths
    article._picture_paths = []
    picture_fields = [
        article.main_picture_max_size,
        article.main_picture_for_article,
        article.main_picture_preview,
        article.main_picture_thumbnail,
    ]

    # Fill the list with values from the article instance
    for field in picture_fields:
        if field and field.name != article.default_picture:
            article._picture_paths.append(field.path)

    # Fill the 'tags_to_delete' attribute with all the article tags
    article.tags_to_delete = list(article.tags.names())

def handle_article_post_delete(article):
    '''
    Handler to capture the post_delete signal for deleting an article.

    The handler works with the '_picture_paths' attribute created in handle_article_pre_delete.
    It iterates through the contents of this list and uses the getattr method to check
    if it contains any values for deletion paths.
    If it does, it first verifies the existence of the file and then deletes it.

    The handler then calls a handler that checks and deletes those tags
    that are not used in any other articles.
    '''

    # Delete images
    for path in getattr(article, '_picture_paths', []):
        if os.path.exists(path):
            os.remove(path)

    # Check and delete unused tags
    handle_delete_unused_tags_post_save(article)
