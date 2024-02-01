### Definuje modely (tabulky) pro kategorie.

from django.db import models
from autoslug import AutoSlugField


class ArticleCategory(models.Model):
    # Název kategorie omezený na 25 znaků
    title = models.CharField(max_length=25)

    # Vytvoření unikátního "slugu" pro URL z názvu kategorie
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        # Textová reprezentace instance (pro administrační rozhraní a výpisy)
        return self.title

    @classmethod
    def get_default_category_id(cls):
        # Implementujte kód pro získání nebo vytvoření výchozí kategorie
        default_category, created = cls.objects.get_or_create(title='Uncategorized')
        return default_category.id