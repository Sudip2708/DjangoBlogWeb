print("### 14 main/articles/models/article_category.py")

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


    @classmethod
    def get_category_id_by_slug(cls, slug):
        """
        Vrací ID kategorie na základě dodaného slugu.

        Args:
            slug (str): Slug kategorie.

        Returns:
            int: ID kategorie, nebo None, pokud kategorie s daným slugem neexistuje.
        """
        try:
            category = cls.objects.get(slug=slug)
            return category.id
        except cls.DoesNotExist:
            return None


    @classmethod
    def get_category_title_by_slug(cls, slug):
        """
        Vrací ID kategorie na základě dodaného slugu.

        Args:
            slug (str): Slug kategorie.

        Returns:
            int: ID kategorie, nebo None, pokud kategorie s daným slugem neexistuje.
        """
        try:
            category = cls.objects.get(slug=slug)
            return category.title
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_all_category_except_default(cls):
        """
        Vrací názvy všech kategorií kromě kategorie s názvem 'Uncategorized'.

        Returns:
            list: Seznam názvů kategorií.
        """

        # Získání kategorie s názvem 'Uncategorized'
        default_category = cls.objects.get(title='Uncategorized')

        # Získání názvů všech kategorií kromě kategorie s názvem 'Uncategorized'
        category_instances = cls.objects.exclude(id=default_category.id)

        return list(category_instances)