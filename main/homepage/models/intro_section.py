from django.utils.translation import gettext_lazy as _
from django.db import models


class HomePageIntroSection(models.Model):

    # Intro Section
    intro_title = models.CharField(
        _('Intro Section Title'),
        max_length=100,
        null=True, blank=True
    )

    intro_description = models.TextField(
        _('Intro Section Description'),
        null=True, blank=True
    )

    def __str__(self):
        return "Homepage Intro Section Configuration"