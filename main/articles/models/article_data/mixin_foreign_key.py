from django.db import models

from taggit.managers import TaggableManager

from ..article_category import ArticleCategory
from ..article_author import ArticleAuthor


class ForeignKeyMixin(models.Model):
    '''
    Mixin for the Article model adding fields related to other models.

    Fields created by this mixin:
    - author: Foreign key to the author of the article.
    - category: Foreign key to the category the article belongs to.
    - tags: Connection to the Taggit module for managing tags.
    - previous_article: Foreign key to the previous article.
    - next_article: Foreign key to the next article.

    The mixin defines an inner Meta class to set abstract behavior.
    (It does not create its own ID or table in the database.)

    The mixin adds an attribute:
    self.tags_to_delete: a list for checking deleted tags
    (it is filled by the clean method in the form and deleted in the post_save signal handle_delete_unused_tags_post_save).
    '''

    author = models.ForeignKey(
        ArticleAuthor,
        verbose_name='Article Author',
        related_name='linked_articles',
        null=True,
        on_delete=models.SET_NULL,
    )

    category = models.ForeignKey(
        ArticleCategory,
        verbose_name='Article Category',
        related_name='linked_articles',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    tags = TaggableManager(
        verbose_name='Article Tag',
        blank=True
    )

    tags_to_delete = []

    previous_article = models.ForeignKey(
        'self',
        verbose_name='Previous Article',
        related_name='previous',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    next_article = models.ForeignKey(
        'self',
        verbose_name='Next Article',
        related_name='next',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True
