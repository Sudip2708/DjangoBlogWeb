from django.db import models

from users.models.custom_user import CustomUser


class ArticleView(models.Model):
    '''
    Model reprezentující zobrazení článku.

    Tento model uchovává informace o zobrazení článku, včetně uživatele, který článek zobrazil,
    a obsahuje následující pole:
    - article: Pole typu ForeignKey, které odkazuje na článek, který byl zobrazen.
    - user: Pole typu ForeignKey, které odkazuje na uživatele, který zobrazil článek.
        (Toto pole může být prázdné pro nepřihlášené uživatele).
    - ip_address: Pole pro IP adresu uživatele, použité pro rozlišení jedinečných přístupů u nepřihlášených uživatelů.
    - created: Pole pro datum a čas vytvoření instance (zobrazení článku).

    Metody modelu:
    - __str__: Získání textové reprezentace modelu (dle hodnoty jména uživatele).
    - record_view: Zaznamená zhlédnutí článku.
    - get_view_count: Vrací počet zhlédnutí článku.
    '''

    article = models.ForeignKey(
        'Article',
        verbose_name='View Article',
        related_name='view_count',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        CustomUser,
        verbose_name='View User',
        related_name='article_view_count',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    ip_address = models.GenericIPAddressField(
        verbose_name='IP Address',
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name='View Created',
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username if self.user else "Anonymous"

    @staticmethod
    def record_view(article, user, ip_address):
        '''
        Statická metoda pro zaznamenání zhlédnutí článku.

        Vytváří novou instanci ArticleView s příslušnými parametry.
        '''
        ArticleView.objects.create(
            article=article,
            user=user if user.is_authenticated else None,
            ip_address=ip_address
        )

    @staticmethod
    def get_view_count(article):
        '''
        Statická metoda pro získání počtu zhlédnutí článku.

        Vrací počet záznamů v ArticleView pro daný článek.
        '''
        return ArticleView.objects.filter(article=article).count()
