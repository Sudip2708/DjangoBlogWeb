from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField

from .article_data.mixin_main_picture import MainPictureMixin
from .article_data.mixin_dates_and_status import DatesAndStatusMixin
from .article_data.mixin_foreign_key import ForeignKeyMixin


class Article(MainPictureMixin, DatesAndStatusMixin, ForeignKeyMixin, models.Model):
    '''
    Model for article data.

    The model inherits from the base class models.Model and adds the following mixins:
    - MainPictureMixin: Mixin containing fields and methods for image processing.
    - DatesAndStatusMixin: Mixin adding fields and methods for date and status processing.
    - ForeignKeyMixin: Mixin adding fields linked to other models.

    In this section, the model creates the following fields:
    - title: Field for the article title.
    - slug: Field for the article slug (used for URL creation).
    - overview: Field for the article overview (only this part is visible in the article preview).
    - content: Field for the article content, which is HTML content created by the TinyMCE module.

    From the mixins, it inherits these fields:
    DatesAndStatusMixin:
    - created: Date of article creation.
    - updated: Date of the last article update.
    - published: Date of article publication.
    - status: Field determining the article status.

    ForeignKeyMixin:
    - author: Foreign key to the article author.
    - category: Foreign key to the category to which the article belongs.
    - tags: Connection to the Taggit module for tag management.
    - previous_article: Foreign key to the previous article.
    - next_article: Foreign key to the next article.

    MainPictureMixin:
    - main_picture_max_size: Largest image size for full-screen display.
    - main_picture_for_article: Medium image size for use on the article page.
    - main_picture_preview: Smaller image size for display on the article list page.
    - main_picture_thumbnail: Thumbnail used for article links.

    Methods added to the model in this section:
    - __str__: For obtaining the textual representation of the model (based on the article name field value).
    - get_absolute_url: For obtaining the URL address of the article.

    Methods inherited from mixins:
    - picture_processing: Method for processing the main image and saving its different sizes.

    The model has several pre_save, post_save, pre_delete, and post_delete signals attached to it,
    processing its content.
    '''

    title = models.CharField(
        verbose_name='Article Title',
        blank=True,
        unique=True,
        max_length=100
    )

    slug = models.SlugField(
        verbose_name='Article Slug',
        blank=True,
        unique=True,
    )

    overview = models.TextField(
        verbose_name='Article Overview',
        blank=True,
        null=True,
    )

    content = HTMLField(
        verbose_name='Article Content',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ''' Returns the absolute URL for displaying the article detail. '''
        return reverse('article-detail', kwargs={'slug': self.slug})
