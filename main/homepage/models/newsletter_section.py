from django.utils.translation import gettext_lazy as _
from django.db import models
from .newsletter_subscriber import NewsletterSubscriber

class HomePageNewsletterSection(models.Model):

    # Newsletter Section
    newsletter_title = models.CharField(
        _('Newsletter Section Title'),
        max_length=100,
        null=True, blank=True
    )

    newsletter_description = models.TextField(
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