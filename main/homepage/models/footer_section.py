from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import JSONField

from .data.singleton_model import SingletonModel
from .data.footer_section_default import DEFAULT_ADDRESS_VALUES
from .data.footer_section_default import DEFAULT_SOCIAL_MEDIA
from .data.footer_section_default import DEFAULT_SITE_LINKS
from .data.footer_section_default import DEFAULT_ARTICLES
from .data.footer_section_default import DEFAULT_END_LINE

class FooterSettings(SingletonModel):
    '''
    Database model for footer settings.

    The model inherits from SingletonModel, which is an abstract class defined
    to create a single instance.

    The model creates the following fields:
    - display_footer_section: Boolean field for representing the display or hiding of the section.
    - address_values: JSONField for storing address-related values.
    - social_media: JSONField for storing social media values.
    - site_links: JSONField for storing links to pages.
    - articles: JSONField for storing a list of articles.
    - end_line: JSONField for storing the content of the footer's last line.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - __init__: Used for initializing default values.
    - get_data: Used to retrieve all the values of this model for rendering on the home page.
    '''

    display_footer_section = models.BooleanField(
        _('Display Footer Section'),
        default=True,
    )

    address_values = JSONField(default=dict)
    social_media = JSONField(default=dict)
    site_links = JSONField(default=dict)
    articles = JSONField(default=dict)
    end_line = JSONField(default=dict)

    def __str__(self):
        return "Footer Configuration"

    def __init__(self, *args, **kwargs):
        '''
        Initialization method of the model.

        This method loads default values for empty fields.
        '''

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


    def get_data(self):
        '''
        Method to retrieve the values of all fields of this model for rendering on the home page.

        Returns a dictionary containing the following information:
        section display, dictionary of address values, social media, links to selected pages,
        selected articles, and the content of the last line.
        '''

        return {
            'display_footer_section': self.display_footer_section,
            'address': self.address_values,
            'social_media': self.social_media,
            'pages_links': self.site_links,
            'articles': self.articles,
            'end_line': self.end_line
        }
