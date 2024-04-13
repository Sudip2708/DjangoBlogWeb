from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import JSONField

from articles.models.article import Article
from .singleton_model import SingletonModel
from .gallery_section_default import DEFAULT_ARTICLE


class HomePageGallerySection(SingletonModel):
    '''
    Databázový model pro gallery sekce na domovské stránce

    Obsahuje pole pro nastavení zobrazení a článků této sekce.
    Metoda __str__ definuje textovou reprezentaci instance tohoto modelu.
    Metoda get_gallery_settings slouží k získání všech hodnot tohoto modelu.

    display_gallery_section - je Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce
    gallery_article_1 - je pole typu JSONField pro uložení dat prvního článku v galerii
    gallery_article_2 - je pole typu JSONField pro uložení dat druhého článku v galerii
    gallery_article_3 - je pole typu JSONField pro uložení dat třetího článku v galerii
    gallery_article_4 - je pole typu JSONField pro uložení dat čtvrtého článku v galerii
    '''

    display_gallery_section = models.BooleanField(
        _('Display Gallery Section'),
        default=True,
    )

    gallery_article_1 = JSONField(default=dict)
    gallery_article_2 = JSONField(default=dict)
    gallery_article_3 = JSONField(default=dict)
    gallery_article_4 = JSONField(default=dict)

    def __str__(self):
        return "Homepage Gallery Section Configuration"

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda modelu.

        Tato metoda načítá defaultní hodnoty, pokud jsou pole prázdná.

        :param args: Pozicinální argumenty.
        :param kwargs: Klíčové argumenty.
        '''

        super().__init__(*args, **kwargs)

        for i in range(1, 5):
            gallery_article_attr = getattr(self, f'gallery_article_{i}')
            if not gallery_article_attr:
                setattr(self, f'gallery_article_{i}', DEFAULT_ARTICLE[f'article_{i}'])


    @property
    def get_gallery_settings(self):
        '''
        Vlastnost, která slouží k získání hodnot všech polí tohoto modelu.

        Vrací slovník obsahující následující informace:
        zobrazení sekce a seznam s daty článků.
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