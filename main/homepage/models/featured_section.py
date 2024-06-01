from django.utils.translation import gettext_lazy as _
from django.db import models

from articles.models.article import Article

from .data.singleton_model import SingletonModel


class HomePageFeaturedArticles(SingletonModel):
    '''
    Databázový model pro Home Page Featured Articles Section.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_divider_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - featured_article_1: Cizí klíč na první doporučený článek, který bude zobrazen v této sekci.
    - featured_article_2: Cizí klíč na druhý doporučený článek, který bude zobrazen v této sekci.
    - featured_article_3: Cizí klíč na třetí doporučený článek, který bude zobrazen v této sekci.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
    '''

    display_featured_section = models.BooleanField(
        _('Display Featured Section'),
        default=True,
    )

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


    def get_data(self):
        '''
        Metoda, která slouží k získání hodnot všech polí tohoto modelu pro vykreslení na domácí stránce.

        Vrací slovník obsahující následující informace:
        zobrazení sekce a seznam článků.
        '''

        return {
            'display_featured_section': self.display_featured_section,
            'articles': [
                self.featured_article_1,
                self.featured_article_2,
                self.featured_article_3
            ],
        }