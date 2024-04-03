from django.db import models

class FooterSettings(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Company Name')
    address = models.CharField(max_length=255, verbose_name='Company Address')
    phone = models.CharField(max_length=20, verbose_name='Company Phone')
    email = models.EmailField(verbose_name='Company Email')
    facebook_url = models.URLField(blank=True, verbose_name='Facebook URL')
    twitter_url = models.URLField(blank=True, verbose_name='Twitter URL')
    instagram_url = models.URLField(blank=True, verbose_name='Instagram URL')
    behance_url = models.URLField(blank=True, verbose_name='Behance URL')
    pinterest_url = models.URLField(blank=True, verbose_name='Pinterest URL')

    class Meta:
        verbose_name = 'Footer Settings'
        verbose_name_plural = 'Footer Settings'

    def __str__(self):
        return self.company_name
