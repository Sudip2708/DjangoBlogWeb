from django.utils.translation import gettext_lazy as _
from django.db import models
from .singleton_model import SingletonModel
from articles.models.article import Article

class FooterSettings(SingletonModel):

    display_footer_section = models.BooleanField(
        _('Display Footer Section'),
        default=True,
    )

    display_footer_end_section = models.BooleanField(
        _('Display Footer End Section'),
        default=True,
    )

    company_name = models.CharField(
        _('Company Name'),
        max_length=100,
        null=True, blank=True
    )

    address = models.CharField(
        _('Company Address'),
        max_length=255,
        null=True, blank=True
    )

    phone = models.CharField(
        _('Company Phone'),
        max_length=20,
        null=True, blank=True
    )

    email = models.EmailField(
        _('Company Email'),
        null = True, blank = True
    )

    # Link to social account
    for social_media in ('Facebook', 'Twitter', 'Instagram', 'Behance', 'Pinterest'):
        locals()[f'{social_media.lower()}_url'] = models.URLField(
            _(f'{social_media} URL'),
            null=True, blank=True
        )

    # Selected pages link
    for number in range(1, 9):
        locals()[f'name_field_{number}'] = models.CharField(
            _(f'Site Link {number} Name'),
            max_length=100,
            null=True, blank=True
        )
        locals()[f'url_field_{number}_url'] = models.URLField(
            _(f'Site Link {number} URL'),
            null=True, blank=True
        )

    # Selected articles
    for number in range(1, 4):
        locals()[f'footer_article_{number}'] = models.ForeignKey(
            Article,
            related_name=f'footer_article_{number}',
            on_delete=models.SET_NULL,
            null=True, blank=True,
            verbose_name=_(f'Footer Article {number}')
        )

    end_right_text = models.CharField(
        _('Footer-End Right Text'),
        max_length=100,
        null=True, blank=True
    )

    end_left_text = models.CharField(
        _('Footer-End Left Text'),
        max_length=100,
        null=True, blank=True
    )

    end_left_link_text = models.CharField(
        _('Footer-End Left Link Text'),
        max_length=100,
        null=True, blank=True
    )

    end_left_link_url = models.URLField(
        _('Footer-End Left Link'),
        default='#!',
        null=True, blank=True
    )


    class Meta:
        verbose_name = 'Footer Settings'
        verbose_name_plural = 'Footer Settings'

    def __str__(self):
        return self.company_name

    @property
    def footer_articles(self):
        """
        Property to return instances of the selected articles.
        """
        footer_articles = []
        for number in range(1, 4):
            footer_articles.append(getattr(self, f'footer_article_{number}', None))
        return footer_articles

    @property
    def footer_address(self):
        """
        Property to return address items.
        """
        address_items = {
            'company_name': self.company_name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
        }
        return address_items

    @property
    def footer_social_links(self):
        """
        Property to return social media links.
        """
        social_media_links = {
            'Facebook': self.facebook_url,
            'Twitter': self.twitter_url,
            'Instagram': self.instagram_url,
            'Behance': self.behance_url,
            'Pinterest': self.pinterest_url,
        }
        return social_media_links


    @property
    def footer_pages_links(self):
        """
        Property to return selected pages links.
        """
        selected_pages_links = {}
        for number in range(1, 9):
            name_field = getattr(self, f'name_field_{number}', None)
            url_field = getattr(self, f'url_field_{number}_url', None)
            if name_field:
                selected_pages_links[name_field] = url_field
        return selected_pages_links


    @property
    def footer_end(self):
        """
        Property to return footer end items.
        """
        address_items = {
            'end_right_text': self.end_right_text,
            'end_left_text': self.end_left_text,
            'end_left_link_text': self.end_left_link_text,
            'end_left_link_url': self.end_left_link_url,
        }
        return address_items

    @property
    def get_footer_settings(self):
        '''
        Navrácení všech hodnot pro vykreslení sekce v Home Page
        '''
        return {
            'display_footer_section': self.display_footer_section,
            'display_footer_end_section': self.display_footer_end_section,
            'address': self.footer_address,
            'social_links': self.footer_social_links,
            'pages_links': self.footer_pages_links,
            'end_line': self.footer_end,
            'articles': self.footer_articles
        }
