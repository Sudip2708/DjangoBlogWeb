from django.utils.text import slugify

from common_data.get_unique_value import get_unique_value
from ...models.article_category import ArticleCategory


def handle_default_values_pre_save(article):
    '''
    Handler to capture the pre_save signal for checking default values.

    The handler checks if it's creating a new instance (the instance doesn't have an assigned ID yet).
    If it is, it checks if the article category is filled.
    If not, it adds the category 'Uncategorized' to the article (category with ID 1 in the ArticleCategory model).
    Then it checks if the article status is filled.
    If not, it adds the status 'drafted' (which is used for creating articles).

    The handler then checks if the article contains a title.
    If not, it calls the 'get_unique_value' function to create a unique name.

    Then the handler checks if the value of the 'slug' field corresponds to the value of the 'title' field for the article title.
    If not, it updates this field with the correct value.
    '''
    # Check if it's creating a new instance
    if not article.id:

        # Create a category if it doesn't exist
        if not article.category:
            article.category = ArticleCategory.objects.get(id=1)

        # Create a status if it doesn't exist
        if not article.status:
            article.status = 'drafted'

    # Create a unique article title
    if not article.title:
        model = article._meta.model
        field = 'title'
        value = f'Article {article.id}'
        article.title = get_unique_value(model, field, value)

    # Check if the slug matches the current title value of the article
    if article.slug != slugify(article.title):
        article.slug = slugify(article.title)
