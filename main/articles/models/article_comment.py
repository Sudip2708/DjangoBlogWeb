### Definuje modely (tabulky) pro komentáře.

from django.db import models
from django.contrib.auth import get_user_model

# Získání modelu uživatele použitého ve vaší aplikaci
User = get_user_model()


class ArticleComment(models.Model):
    # Cizí klíč na uživatele, který vytvořil komentář
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Datum a čas vytvoření komentáře
    created = models.DateTimeField(auto_now_add=True)

    # Obsah komentáře
    content = models.TextField()

    # Cizí klíč na článek, ke kterému je komentář připojen
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        # Textová reprezentace instance (pro administrační rozhraní a výpisy)
        return self.user.username
