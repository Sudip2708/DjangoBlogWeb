from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import JSONField

from articles.models.article import Article
from .singleton_model import SingletonModel
from .gallery_section_default import DEFAULT_ARTICLE


class HomePageGallerySection(SingletonModel):

    display_gallery_section = models.BooleanField(
        _('Display Gallery Section'),
        default=True,
    )

    # Gallery Section
    gallery_article_1 = JSONField(default=dict)

    gallery_article_2 = JSONField(default=dict)

    gallery_article_3 = JSONField(default=dict)

    gallery_article_4 = JSONField(default=dict)

    def __str__(self):
        return "Homepage Gallery Section Configuration"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Cyklus pro přidání defaultních hodnot (jen pokud nejsou zadané žádné hodnoty v databázy)
        for i in range(1, 5):
            gallery_article_attr = getattr(self, f'gallery_article_{i}')
            if not gallery_article_attr:
                setattr(self, f'gallery_article_{i}', DEFAULT_ARTICLE[f'article_{i}'])


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
        print("### self.gallery_articles: ", self.gallery_articles)

        return {
            'display_gallery_section': self.display_gallery_section,
            'articles': self.gallery_articles,
        }