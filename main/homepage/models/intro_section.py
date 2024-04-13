from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .singleton_model import SingletonModel


class HomePageIntroSection(SingletonModel):
    '''
    Databázový model pro Home Page Intro Section

    Obsahuje pole pro nastavení zobrazení této sekce, nadpisu a textu.
    Metoda __str__ definuje textovou reprezentaci instance tohoto modelu.
    Metoda get_intro_settings slouží k získání všech hodnot tohoto modelu.

    display_intro_section - je Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce
    intro_title - je HTML pole pro vložení nadpisu, který bude zobrazen v této sekci
    intro_description - je HTML pole pro vložení textu, který bude zobrazen v této sekci
    '''

    display_intro_section = models.BooleanField(
        _('Display Intro Section'),
        default=True,
    )

    # Intro Section
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

    @property
    def get_intro_settings(self):
        '''
        Vlastnost, která slouží k získání hodnot všech polí tohoto modelu.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, nadpisu a popisu sekce.
        '''

        return {
            'display_intro_section': self.display_intro_section,
            'intro_title': self.intro_title,
            'intro_description': self.intro_description,
        }