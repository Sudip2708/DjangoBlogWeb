from django.db import models
from users.models import CustomUser

class NewsletterSubscriber(models.Model):
    '''
    Databázový model pro uchovávání informací o zájemcích o zasílání novinek.

    Obsahuje pole pro e-mailovou adresu, odkaz na uživatele, který se přihlásil k odběru (v případě, že existuje),
    a datum, kdy se uživatel přihlásil k odběru.
    Metoda __str__ definuje textovou reprezentaci instance tohoto modelu.
    Třída Meta určuje lidsky čitelné jméno modelu v jednotném a množném čísle.

    email - je pole pro uchování e-mailové adresy zájemce o zasílání novinek
    user - je ForeignKey pole pro propojení s modelem CustomUser, pokud se uživatel přihlásil k odběru
    subscribed_at - je pole typu DateTimeField, které uchovává datum a čas přihlášení k odběru
    '''

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

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'
