from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .data.singleton_model import SingletonModel


class HomePageIntroSection(SingletonModel):
    '''
    Databázový model pro Home Page Intro Section.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_intro_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - intro_title: HTML pole pro vložení nadpisu, který bude zobrazen v této sekci.
    - intro_description: HTML pole pro vložení textu, který bude zobrazen v této sekci.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
    '''

    display_intro_section = models.BooleanField(
        _('Display Intro Section'),
        default=True,
    )

    intro_title = HTMLField(
        _('Intro Section Title'),
        default="<div><span style='font-size: 28px;'><strong>Some great intro here</strong></span></div>",
        null=True, blank=True
    )

    intro_description = HTMLField(
        _('Intro Section Description'),
        default="<div style='line-height: 2;'><span style='font-size: 16.5pt; color: rgb(0, 0, 0);'><span style='color: rgb(33, 33, 33);'>Place a nice&nbsp;</span><strong>introduction</strong><span style='color: rgb(33, 33, 33);'>&nbsp;here</span>&nbsp;<strong>to catch reader's attention</strong>. <span style='color: rgb(33, 33, 33);'>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderi.</span></span></div>",
        null=True, blank=True
    )

    def __str__(self):
        return "Homepage Intro Section Configuration"

    def get_data(self):
        '''
        Metoda, která slouží k získání hodnot všech polí tohoto modelu pro vykreslení na domácí stránce.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, nadpisu a popisu sekce.
        '''

        return {
            'display_intro_section': self.display_intro_section,
            'intro_title': self.intro_title,
            'intro_description': self.intro_description,
        }