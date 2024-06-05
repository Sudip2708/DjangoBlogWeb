from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .newsletter_subscriber import NewsletterSubscriber
from .data.singleton_model import SingletonModel


class HomePageNewsletterSection(SingletonModel):
    '''
    Database model for the Home Page Newsletter Section.

    The model inherits from SingletonModel, which is an abstract class defined to create a single instance.

    The model creates the following fields:
    - display_newsletter_section: Boolean field for representing the display or hiding of the section.
    - newsletter_title: HTML field for inserting a title to be displayed in this section.
    - newsletter_description: HTML field for inserting a description to be displayed in this section.
    - newsletter_subscribers: ForeignKey field for linking with the NewsletterSubscriber model and storing newsletter subscribers.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - get_data: Used to retrieve all the editable fields' values of this model for rendering on the home page.
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
        Method to retrieve the values of all editable fields of this model for rendering on the home page.

        Returns a dictionary containing the following information:
        section display, section title, and section description.
        '''

        return {
            'display_newsletter_section': self.display_newsletter_section,
            'newsletter_title': self.newsletter_title,
            'newsletter_description': self.newsletter_description,
        }
