from django.db import models

from users.models.custom_user import CustomUser


class NewsletterSubscriber(models.Model):
    '''
    Databázový model pro uchovávání informací o zájemcích o zasílání novinek.

    Model dědí z třídy models.Model a vytváří následující pole:
    - email: Pole pro uchování e-mailové adresy zájemce o zasílání novinek
    - user: ForeignKey pole pro propojení s modelem CustomUser, pokud se uživatel přihlásil k odběru
    - subscribed_at: Pole typu DateTimeField, které uchovává datum a čas přihlášení k odběru

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - class Meta: Určuje lidsky čitelné jméno modelu v jednotném a množném čísle.
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
