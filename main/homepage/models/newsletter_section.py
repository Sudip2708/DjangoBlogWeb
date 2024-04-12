from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .newsletter_subscriber import NewsletterSubscriber
from .singleton_model import SingletonModel


class HomePageNewsletterSection(SingletonModel):
    '''
    Databázový model pro Home Page Newsletter Section

    Obsahuje pole pro nastavení zobrazení této sekce, nadpisu, popisu a pole prozadávání emailů.
    Pole pro zadávání emailu je provázané s modelem NewsletterSubscriber.
    Metoda __str__ definuje textovou reprezentaci instance tohoto modelu.
    Metoda get_divider_settings slouží k získání všech editovatelných hodnot tohoto modelu.
    '''

    display_newsletter_section = models.BooleanField(
        _('Display Newsletter Section'),
        default=True,
    )

    # Newsletter Section
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

    @property
    def get_newsletter_settings(self):
        '''
        Vlastnost, která slouží k získání hodnot všech editovatelných polí tohoto modelu.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, nadpis a popis sekce.
        '''

        return {
            'display_newsletter_section': self.display_newsletter_section,
            'newsletter_title': self.newsletter_title,
            'newsletter_description': self.newsletter_description,
        }