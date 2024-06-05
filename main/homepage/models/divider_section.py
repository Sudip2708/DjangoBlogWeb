from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField

from .data.singleton_model import SingletonModel


class HomePageDividerSection(SingletonModel):
    '''
    Database model for the Home Page Divider Section.

    The model inherits from SingletonModel, which is an abstract class defined
    to create a single instance.

    The model creates the following fields:
    - display_divider_section: Boolean field for representing the display or hiding of the section.
    - divider_image: Field for uploading an image to be displayed in this section.
    - divider_text: HTML field for inserting text to be displayed in this section.
    - divider_link_title: CharField for the title of the link to be displayed in this section.
    - divider_link: URLField for inserting the URL link to be displayed in this section.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - get_data: Used to retrieve all the values of this model for rendering on the home page.
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
        _('Divider Section Link Title'),
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

    def get_data(self):
        '''
        Method to retrieve the values of all fields of this model for rendering on the home page.

        If an image for the divider is not available, its URL will be None.
        Returns a dictionary containing the following information:
        section display, image URL, section text, link description, and link URL.
        '''

        # Assign None if there is no image
        divider_image_url = self.divider_image.url if self.divider_image else None

        return {
            'display_divider_section': self.display_divider_section,
            'divider_image': divider_image_url,
            'divider_text': self.divider_text,
            'divider_link_title': self.divider_link_title,
            'divider_link': self.divider_link,
        }
