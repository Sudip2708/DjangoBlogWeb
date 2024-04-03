from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article

class HomePageLatestArticles(models.Model):

    # Latest Articles
    latest_title = models.CharField(
        _('Latest Articles Title'),
        max_length=100,
        null=True, blank=True
    )

    latest_description = models.TextField(
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