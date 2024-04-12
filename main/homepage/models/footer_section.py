from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import JSONField

from .singleton_model import SingletonModel
from .footer_section_default import DEFAULT_ADDRESS_VALUES
from .footer_section_default import DEFAULT_SOCIAL_MEDIA
from .footer_section_default import DEFAULT_SITE_LINKS
from .footer_section_default import DEFAULT_ARTICLES
from .footer_section_default import DEFAULT_END_LINE


class FooterSettings(SingletonModel):

    display_footer_section = models.BooleanField(
        _('Display Footer Section'),
        default=True,
    )

    address_values = JSONField(default=dict)
    social_media = JSONField(default=dict)
    site_links = JSONField(default=dict)
    articles = JSONField(default=dict)
    end_line = JSONField(default=dict)


    class Meta:
        verbose_name = 'Footer Settings'
        verbose_name_plural = 'Footer Settings'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.address_values:
            self.address_values = DEFAULT_ADDRESS_VALUES
        if not self.social_media:
            self.social_media = DEFAULT_SOCIAL_MEDIA
        if not self.site_links:
            self.site_links = DEFAULT_SITE_LINKS
        if not self.articles:
            self.articles = DEFAULT_ARTICLES
        if not self.end_line:
            self.end_line = DEFAULT_END_LINE

    @property
    def get_footer_settings(self):
        '''
        Return all footer settings as a dictionary.
        '''

        return {
            'display_footer_section': self.display_footer_section,
            'address': self.address_values,
            'social_media': self.social_media,
            'pages_links': self.site_links,
            'end_line': self.end_line,
            'articles': self.articles
        }
