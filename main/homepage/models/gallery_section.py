from django.utils.translation import gettext_lazy as _
from django.db import models

from articles.models.article import Article
from .data.singleton_model import SingletonModel


class HomePageGallerySection(SingletonModel):
    '''
    Database model for the gallery section on the home page.

    The model inherits from SingletonModel, which is an abstract class defined to create a single instance.

    The model creates the following fields:
    - display_gallery_section: Boolean field for representing the display or hiding of the section.
    - gallery_article_1: JSONField for storing data of the first article in the gallery.
    - gallery_article_2: JSONField for storing data of the second article in the gallery.
    - gallery_article_3: JSONField for storing data of the third article in the gallery.
    - gallery_article_4: JSONField for storing data of the fourth article in the gallery.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - __init__: Used for initializing default values.
    - get_data: Used to retrieve all the values of this model for rendering on the home page.
    '''

    display_gallery_section = models.BooleanField(
        _('Display Gallery Section'),
        default=True,
    )

    gallery_article_1 = models.ForeignKey(
        Article,
        related_name='gallery_article_1',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Gallery Article 1')
    )

    gallery_article_2 = models.ForeignKey(
        Article,
        related_name='gallery_article_2',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Gallery Article 2')
    )

    gallery_article_3 = models.ForeignKey(
        Article,
        related_name='gallery_article_3',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Gallery Article 3')
    )

    gallery_article_4 = models.ForeignKey(
        Article,
        related_name='gallery_article_4',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Gallery Article 4')
    )

    def __str__(self):
        return "Homepage Gallery Section Configuration"


    def get_data(self):
        '''
        Method to retrieve the values of all fields of this model for rendering on the home page.

        Returns a dictionary containing the following information:
        section display and a list with data of gallery articles.
        '''

        return {
            'display_gallery_section': self.display_gallery_section,
            'articles': [
                self.gallery_article_1,
                self.gallery_article_2,
                self.gallery_article_3,
                self.gallery_article_4,
            ],
        }
