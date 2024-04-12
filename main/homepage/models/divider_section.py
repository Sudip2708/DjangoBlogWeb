from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .singleton_model import SingletonModel


class HomePageDividerSection(SingletonModel):
    '''
    Databázový model pro Home Page Divider Section

    Obsahuje pole pro nastavení zobrazení této sekce, obrázku, textu a odkazu.
    Metoda __str__ definuje textovou reprezentaci instance tohoto modelu.
    Metoda get_divider_settings slouží k získání všech hodnot tohoto modelu.
    '''

    display_divider_section = models.BooleanField(
        _('Display Divider Section'),
        default=True,
    )

    divider_image = models.ImageField(
        _('Divider Section Image'),
        default='images/homepage/default/divider-bg.jpg',
        upload_to='images/homepage/',
        null=True, blank=True
    )

    divider_text = HTMLField(
        _('Divider Section Text'),
        default=("<h2>Lorem ipsum dolor sit amet, consectetur adipisicing elit, " +
                 "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</h2>"),
        null=True, blank=True
    )

    divider_link_title = models.CharField(
        _('Hero Section Link Title'),
        default='View More',
        max_length=100,
        null=True, blank=True
    )

    divider_link = models.URLField(
        _('Divider Section Link'),
        default='#!',
        null=True, blank=True
    )

    def __str__(self):
        return "Homepage Divider Section Configuration"

    @property
    def get_divider_settings(self):
        '''
        Vlastnost, která slouží k získání hodnot všech polí tohoto modelu.

        Pokud není k dispozici obrázek pro oddělovač, jeho URL bude None.
        Vrací slovník obsahující následující informace:
        zobrazení sekce, URL obrázku, text sekce, popis odkazu a URL odkazu.
        '''

        # Dosazení hodnoty None, když není obrázek
        divider_image_url = self.divider_image.url if self.divider_image else None

        return {
            'display_divider_section': self.display_divider_section,
            'divider_image': divider_image_url,
            'divider_text': self.divider_text,
            'divider_link_title': self.divider_link_title,
            'divider_link': self.divider_link,
        }