from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .newsletter_subscriber import NewsletterSubscriber
from .data.singleton_model import SingletonModel


class HomePageNewsletterSection(SingletonModel):
    '''
    Databázový model pro Home Page Newsletter Section.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_newsletter_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - newsletter_title: HTML pole pro vložení nadpisu, který bude zobrazen v této sekci
    - newsletter_description: HTML pole pro vložení popisu, který bude zobrazen v této sekci
    - newsletter_subscribers: ForeignKey pole pro propojení s modelem NewsletterSubscriber a ukládání odběratelů newsletteru.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
    '''

    display_newsletter_section = models.BooleanField(
        _('Display Newsletter Section'),
        default=True,
    )

    newsletter_title = HTMLField(
        _('Newsletter Section Title'),
        null=True, blank=True
    )

    newsletter_description = HTMLField(
        _('Newsletter Section Description'),
        null=True, blank=True
    )

    newsletter_subscribers = models.ForeignKey(
        NewsletterSubscriber,
        on_delete=models.CASCADE,
        related_name='home_page_subscribers',
        blank=True, null=True,
        verbose_name=_('Newsletter Subscribers')
    )

    def __str__(self):
        return "Homepage Newsletter Section Configuration"

    def get_data(self):
        '''
        Metoda, která slouží k získání hodnot všech editovatelných polí tohoto modelu pro vykreslení na domácí stránce.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, nadpis a popis sekce.
        '''

        return {
            'display_newsletter_section': self.display_newsletter_section,
            'newsletter_title': self.newsletter_title,
            'newsletter_description': self.newsletter_description,
        }