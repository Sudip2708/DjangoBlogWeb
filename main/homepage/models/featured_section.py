from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article
from .singleton_model import SingletonModel


class HomePageFeaturedArticles(SingletonModel):

    display_featured_section = models.BooleanField(
        _('Display Featured Section'),
        default=True,
    )

    # Featured articles
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

    @property
    def featured_articles(self):
        """
        Property to return instances of the featured articles.
        """
        return [
            self.featured_article_1,
            self.featured_article_2,
            self.featured_article_3
        ]

    def __str__(self):
        return "Homepage Featured Articles Configuration"

    @property
    def get_featured_settings(self):
        '''
        Navrácení všech hodnot pro vykreslení sekce v Home Page
        '''

        return {
            'display_featured_section': self.display_featured_section,
            'articles': self.featured_articles,
        }