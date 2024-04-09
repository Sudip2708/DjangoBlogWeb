from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article
from .singleton_model import SingletonModel


class HomePageGallerySection(SingletonModel):

    display_gallery_section = models.BooleanField(
        _('Display Gallery Section'),
        default=True,
    )

    # Gallery Section
    gallery_article_1 = models.ForeignKey(
        Article,
        related_name='gallery_article_1',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Home Page Gallery Article 1')
    )

    gallery_article_2 = models.ForeignKey(
        Article,
        related_name='gallery_article_2',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Home Page Gallery Article 2')
    )

    gallery_article_3 = models.ForeignKey(
        Article,
        related_name='gallery_article_3',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Home Page Gallery Article 3')
    )

    gallery_article_4 = models.ForeignKey(
        Article,
        related_name='gallery_article_4',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Home Page Gallery Article 4')
    )

    def __str__(self):
        return "Homepage Gallery Section Configuration"

    @property
    def gallery_articles(self):
        """
        Property to return instances of the featured articles.
        """
        return [
            self.gallery_article_1,
            self.gallery_article_2,
            self.gallery_article_3,
            self.gallery_article_4,
        ]

    @property
    def get_gallery_settings(self):
        '''
        Navrácení všech hodnot pro vykreslení sekce v Home Page
        '''

        return {
            'display_gallery_section': self.display_gallery_section,
            'articles': self.gallery_articles,
        }