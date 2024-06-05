from django.utils.translation import gettext_lazy as _
from django.db import models

from articles.models.article import Article

from .data.singleton_model import SingletonModel


class HomePageFeaturedArticles(SingletonModel):
    '''
    Database model for the Home Page Featured Articles Section.

    The model inherits from SingletonModel, which is an abstract class defined
    to create a single instance.

    The model creates the following fields:
    - display_featured_section: Boolean field for representing the display or hiding of the section.
    - featured_article_1: Foreign key to the first featured article to be displayed in this section.
    - featured_article_2: Foreign key to the second featured article to be displayed in this section.
    - featured_article_3: Foreign key to the third featured article to be displayed in this section.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - get_data: Used to retrieve all the values of this model for rendering on the home page.
    '''

    display_featured_section = models.BooleanField(
        _('Display Featured Section'),
        default=True,
    )

    featured_article_1 = models.ForeignKey(
        Article,
        related_name='featured_article_1',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Featured Article 1')
    )

    featured_article_2 = models.ForeignKey(
        Article,
        related_name='featured_article_2',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Featured Article 2')
    )

    featured_article_3 = models.ForeignKey(
        Article,
        related_name='featured_article_3',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Featured Article 3')
    )

    def __str__(self):
        return "Homepage Featured Articles Configuration"


    def get_data(self):
        '''
        Method to retrieve the values of all fields of this model for rendering on the home page.

        Returns a dictionary containing the following information:
        section display and a list of articles.
        '''

        return {
            'display_featured_section': self.display_featured_section,
            'articles': [
                self.featured_article_1,
                self.featured_article_2,
                self.featured_article_3
            ],
        }
