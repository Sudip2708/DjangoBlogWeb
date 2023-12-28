### Definuje modely (tabulky) pro autora článku.

from django.db import models
from django.contrib.auth import get_user_model

# Získání modelu uživatele použitého ve vaší aplikaci
User = get_user_model()


class ArticleAuthor(models.Model):
    # Vytvoření vztahu "one-to-one" s modelem uživatele
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    # Obrázek profilového obrázku pro autora článku
    profile_picture = models.ImageField()

    def __str__(self):
        # Textová reprezentace instance (pro administrační rozhraní a výpisy)
        return self.author.username
