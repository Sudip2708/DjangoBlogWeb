from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import JSONField

from .data.singleton_model import SingletonModel
from .data.footer_section_default import DEFAULT_ADDRESS_VALUES
from .data.footer_section_default import DEFAULT_SOCIAL_MEDIA
from .data.footer_section_default import DEFAULT_SITE_LINKS
from .data.footer_section_default import DEFAULT_ARTICLES
from .data.footer_section_default import DEFAULT_END_LINE

class FooterSettings(SingletonModel):
    '''
    Databázový model pro nastavení patičky.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_footer_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - address_values: Pole typu JSONField pro uložení hodnot týkajících se adresy.
    - social_media: Pole typu JSONField pro uložení hodnot sociálních médií.
    - site_links: Pole typu JSONField pro uložení odkazů na stránky.
    - articles: Pole typu JSONField pro uložení seznamu článků.
    - end_line: Pole typu JSONField pro uložení obsahu posledního řádku patičky.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - __init__: Slouží pro inicializaci defaultních hodnot.
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
    '''

    display_footer_section = models.BooleanField(
        _('Display Footer Section'),
        default=True,
    )

    address_values = JSONField(default=dict)
    social_media = JSONField(default=dict)
    site_links = JSONField(default=dict)
    articles = JSONField(default=dict)
    end_line = JSONField(default=dict)

    def __str__(self):
        return "Footer Configuration"

    def __init__(self, *args, **kwargs):
        '''
        Inicializační metoda modelu.

        Tato metoda načítá defaultní hodnoty pro prázdná pole.
        '''

        super().__init__(*args, **kwargs)

        if not self.address_values:
            self.address_values = DEFAULT_ADDRESS_VALUES
        if not self.social_media:
            self.social_media = DEFAULT_SOCIAL_MEDIA
        if not self.site_links:
            self.site_links = DEFAULT_SITE_LINKS
        if not self.articles:
            self.articles = DEFAULT_ARTICLES
        if not self.end_line:
            self.end_line = DEFAULT_END_LINE


    def get_data(self):
        '''
        Metoda, která slouží k získání hodnot všech polí tohoto modelu pro vykreslení na domácí stránce.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, slovníku hodnot pro adresu, sociální média, odkazy na vybrané stránky,
        vybrané články a obsah posledního řádku.
        '''

        return {
            'display_footer_section': self.display_footer_section,
            'address': self.address_values,
            'social_media': self.social_media,
            'pages_links': self.site_links,
            'articles': self.articles,
            'end_line': self.end_line
        }
