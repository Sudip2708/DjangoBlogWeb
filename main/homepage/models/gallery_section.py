from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article

class HomePageGallerySection(models.Model):

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