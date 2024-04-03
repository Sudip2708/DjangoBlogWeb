from django.utils.translation import gettext_lazy as _
from django.db import models


class HomePageHeroSection(models.Model):


    hero_image = models.ImageField(
        _('Hero Section Image'),
        default='images/homepage/default/hero.jpg',
        upload_to='images/homepage/',
        null=True, blank=True
    )

    hero_title = models.CharField(
        _('Hero Section Title'),
        default='Bootstrap 5 Blog - A free template by Bootstrapious',
        max_length=100,
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