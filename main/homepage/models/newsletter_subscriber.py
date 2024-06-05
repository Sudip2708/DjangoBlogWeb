from django.db import models

from users.models.custom_user import CustomUser


class NewsletterSubscriber(models.Model):
    '''
    Database model for storing information about newsletter subscribers.

    The model inherits from the models.Model class and creates the following fields:
    - email: Field for storing the email address of the newsletter subscriber.
    - user: ForeignKey field for linking with the CustomUser model if the user has subscribed.
    - subscribed_at: DateTimeField field that stores the date and time of subscription.

    Model methods:
    - __str__: To get the textual representation of the model (based on the email field value).
    - class Meta: Specifies the human-readable name of the model in singular and plural forms.
    '''

    email = models.EmailField(
        unique=True,
        verbose_name='Email Address'
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Subscribed User',
        related_name='newsletter_subscriptions'
    )

    subscribed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Subscription Date'
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
