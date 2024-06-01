from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField
from .data.singleton_model import SingletonModel


class HomePageHeroSection(SingletonModel):
    '''
    Databázový model pro Home Page Hero Section.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_hero_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - hero_image: Pole pro upload obrázku, který bude zobrazen v této sekci.
    - hero_title: HTML pole pro vložení textu, který bude zobrazen v této sekci.
    - hero_link_title: Pole typu CharField pro titulek odkazu, který bude zobrazen v této sekci.
    - hero_link: Pole typu URLField pro vložení URL odkazu, který bude zobrazen v této sekci.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
    '''

    display_hero_section = models.BooleanField(
        _('Display Hero Section'),
        default=True,
    )

    hero_image = models.ImageField(
        _('Hero Section Image'),
        default='images/homepage/default/hero.jpg',
        upload_to='images/homepage/',
        null=True, blank=True
    )

    hero_title = HTMLField(
        _('Hero Section Title'),
        default="<h1>Bootstrap 5 Blog - A free template by Bootstrapious</h1>",
        null=True, blank=True
    )

    hero_link_title = models.CharField(
        _('Hero Section Link Title'),
        default='Discover More',
        max_length=100,
        null=True, blank=True
    )

    hero_link = models.URLField(
        _('Hero Section Link'),
        default='#!',
        null=True, blank=True
    )

    def __str__(self):
        return "Homepage Hero Section Configuration"

    def get_data(self):
        '''
        Metoda, která slouží k získání hodnot všech polí tohoto modelu pro vykreslení na domácí stránce.

        Pokud není k dispozici obrázek pro oddělovač, jeho URL bude None.
        Vrací slovník obsahující následující informace:
        zobrazení sekce, URL obrázku, nadpis sekce, popisu odkazu a URL odkazu.
        '''

        # Dosazení hodnoty None, když není obrázek
        hero_image_url = self.hero_image.url if self.hero_image else None

        return {
            'display_hero_section': self.display_hero_section,
            'hero_image': hero_image_url,
            'hero_title': self.hero_title,
            'hero_link_title': self.hero_link_title,
            'hero_link': self.hero_link,
        }




