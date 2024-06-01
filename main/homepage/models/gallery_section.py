from django.utils.translation import gettext_lazy as _
from django.db import models

from articles.models.article import Article
from .data.singleton_model import SingletonModel


class HomePageGallerySection(SingletonModel):
    '''
    Databázový model pro gallery sekce na domovské stránce.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_gallery_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - gallery_article_1: Pole typu JSONField pro uložení dat prvního článku v galerii.
    - gallery_article_2: Pole typu JSONField pro uložení dat druhého článku v galerii.
    - gallery_article_3: Pole typu JSONField pro uložení dat třetího článku v galerii.
    - gallery_article_4: Pole typu JSONField pro uložení dat čtvrtého článku v galerii.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - __init__: Slouží pro inicializaci defaultních hodnot.
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
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
        Metoda, která slouží k získání hodnot všech polí tohoto modelu pro vykreslení na domácí stránce.

        Vrací slovník obsahující následující informace:
        zobrazení sekce a seznam s daty článků galerie.
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