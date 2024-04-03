from django.db import models
from users.models import CustomUser

class NewsletterSubscriber(models.Model):

    email = models.EmailField(
        unique=True,
        verbose_name='Email Address'
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Subscribed User'
    )

    subscribed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Subscription Date'
    )

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'

    def __str__(self):
        return self.email
