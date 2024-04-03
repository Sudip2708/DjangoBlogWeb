from django.utils.translation import gettext_lazy as _
from django.db import models


class HomePageDividerSection(models.Model):

    # Divider Section
    divider_image = models.ImageField(
        _('Divider Section Image'),
        upload_to='images/homepage/',
        null=True, blank=True
    )

    divider_text = models.TextField(
        _('Divider Section Text'),
        null=True, blank=True
    )

    divider_link = models.URLField(
        _('Divider Section Link'),
        null=True, blank=True
    )

    def __str__(self):
        return "Homepage Divider Section Configuration"