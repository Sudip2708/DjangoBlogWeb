from django.db import models

from users.models.custom_user import CustomUser


class ArticleComment(models.Model):
    '''
    Model reprezentující komentář k článku.

    Tento model uchovává informace o komentáři, který uživatel přidal k článku,
    a obsahuje následující pole:
    - article: Pole typu ForeignKey, které odkazuje na článek, ke kterému je komentář připojen.
    - user: Pole typu ForeignKey, které odkazuje na uživatele, který vytvořil komentář.
    - content: Pole pro obsah komentáře.
    - created: Pole pro datum a čas vytvoření komentáře.

    Metody modelu:
    - __str__: Získání textové reprezentace modelu (dle hodnoty jména uživatele).
    '''

    article = models.ForeignKey(
        'Article',
        verbose_name='Comment Article',
        related_name='comments',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        CustomUser,
        verbose_name='Comment User',
        related_name='user_comments',
        null=True,
        on_delete=models.SET_NULL,
    )

    content = models.TextField(
        verbose_name='Comment Content',
    )

    created = models.DateTimeField(
        verbose_name='Comment Created',
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username
