from django.utils.translation import gettext_lazy as _
from django.db import models
from tinymce.models import HTMLField
from .singleton_model import SingletonModel


class HomePageHeroSection(SingletonModel):

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

    @property
    def get_hero_settings(self):
        '''
        Navrácení všech hodnot pro vykreslení sekce v Home Page
        '''

        # Dosazení defaultního obrázku, když není
        # hero_image_url = self.hero_image.url if self.hero_image else self._meta.get_field('hero_image').get_default()
        # Dosazení None, když není obrázek
        hero_image_url = self.hero_image.url if self.hero_image else None

        return {
            'display_hero_section': self.display_hero_section,
            'hero_image': hero_image_url,
            'hero_title': self.hero_title,
            'hero_link_title': self.hero_link_title,
            'hero_link': self.hero_link,
        }