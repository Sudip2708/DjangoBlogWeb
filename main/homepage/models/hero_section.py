from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField
from .data.singleton_model import SingletonModel


class HomePageHeroSection(SingletonModel):
    '''
    Database model for the Home Page Hero Section.

    The model inherits from SingletonModel, which is an abstract class defined to create a single instance.

    The model creates the following fields:
    - display_hero_section: Boolean field for representing the display or hiding of the section.
    - hero_image: Field for uploading an image to be displayed in this section.
    - hero_title: HTML field for inserting text to be displayed in this section.
    - hero_link_title: CharField for the title of the link to be displayed in this section.
    - hero_link: URLField for inserting the URL link to be displayed in this section.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - get_data: Used to retrieve all the values of this model for rendering on the home page.
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
        Method to retrieve the values of all fields of this model for rendering on the home page.

        If there is no image for the divider, its URL will be None.
        Returns a dictionary containing the following information:
        section display, URL of the image, section title, link description, and URL of the link.
        '''

        # Assigning None if there is no image
        hero_image_url = self.hero_image.url if self.hero_image else None

        return {
            'display_hero_section': self.display_hero_section,
            'hero_image': hero_image_url,
            'hero_title': self.hero_title,
            'hero_link_title': self.hero_link_title,
            'hero_link': self.hero_link,
        }
