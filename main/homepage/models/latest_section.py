from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article
from .singleton_model import SingletonModel
from tinymce.models import HTMLField


class HomePageLatestArticles(SingletonModel):

    display_latest_section = models.BooleanField(
        _('Display Latest Section'),
        default=True,
    )

    # Latest Articles
    latest_title = HTMLField(
        _('Latest Articles Title'),
        null=True, blank=True
    )

    latest_description = HTMLField(
        _('Latest Articles Description'),
        null=True, blank=True
    )

    latest_article_1 = models.ForeignKey(
        Article,
        related_name='latest_article_1',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Latest Article 1')
    )

    latest_article_2 = models.ForeignKey(
        Article,
        related_name='latest_article_2',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Latest Article 2')
    )

    latest_article_3 = models.ForeignKey(
        Article,
        related_name='latest_article_3',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Latest Article 3')
    )



    def __str__(self):
        return "Homepage Latest Articles Configuration"


    @property
    def latest_articles(self):
        """
        Property to return instances of the featured articles.
        """
        latest_articles = list(Article.objects.filter(status='publish').order_by('-created')[:3])

        # Check if any of the latest articles are already assigned
        assigned_articles = [
            self.latest_article_1,
            self.latest_article_2,
            self.latest_article_3
        ]

        # First loop: Check if any assigned articles are already in the latest articles list
        for index, article in enumerate(assigned_articles):
            if article in latest_articles:
                latest_articles = [a for a in latest_articles if a != article]

        # Second loop: Fill null fields with the latest articles
        for index, article in enumerate(assigned_articles):
            if article is None:
                assigned_articles[index] = latest_articles.pop(0)


        return assigned_articles

    @property
    def get_latest_settings(self):
        '''
        Navrácení všech hodnot pro vykreslení sekce v Home Page
        '''

        return {
            'display_latest_section': self.display_latest_section,
            'latest_title': self.latest_title,
            'latest_description': self.latest_description,
            'articles': self.latest_articles,
        }