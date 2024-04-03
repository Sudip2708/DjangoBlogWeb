from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article

class HomePageFeaturedArticles(models.Model):

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


    def __str__(self):
        return "Homepage Featured Articles Configuration"