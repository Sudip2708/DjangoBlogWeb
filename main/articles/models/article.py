### Definuje modely (tabulky) pro článek.

from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

from .article_author import ArticleAuthor
from .article_category import ArticleCategory
from articles.models.article_view import ArticleView


class Article(models.Model):
    # Cizí klíč na autora článku
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE)

    # Název článku, omezený na 100 znaků
    title = models.CharField(max_length=100)

    # Automaický generovaný slug pro URL na základě názvu článku, unikátní
    slug = AutoSlugField(populate_from='title', unique=True)

    # Krátký popis článku
    overview = models.TextField()

    # Obsah článku v HTML formátu
    content = HTMLField()

    # Obrázek reprezentující článek
    thumbnail = models.ImageField()

    # Datum vytvoření článku
    created = models.DateTimeField(auto_now_add=True)

    # Datum poslední aktualizace článku
    updated = models.DateTimeField(auto_now=True)

    # Správce pro práci s tagy
    tags = TaggableManager()

    # Množina kategorií, ke kterým článek patří
    categories = models.ManyToManyField(ArticleCategory)

    # Počet komentářů k článku
    comment_count = models.PositiveIntegerField(default=0)

    # Příznak, zda je článek označený jako "featured"
    featured = models.BooleanField(default=False)

    # Odkazy na předchozí a následující článek
    previous_article = models.ForeignKey(
        'self',
        related_name='previous',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    next_article = models.ForeignKey(
        'self',
        related_name='next',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        # Index pro rychlejší vyhledávání podle slugu
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        # Textová reprezentace instance (pro administrační rozhraní a výpisy)
        return self.title

    def get_absolute_url(self):
        # Vrátí absolutní URL pro zobrazení detailu článku
        return reverse('article-detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        # Vrátí URL pro aktualizaci článku
        return reverse('article-update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        # Vrátí URL pro smazání článku
        return reverse('article-delete', kwargs={'slug': self.slug})

    @property
    def get_comments(self):
        # Vrátí všechny komentáře k článku, seřazené sestupně podle data vytvoření
        return self.comments.all().order_by('-created')

    @property
    def view_count(self):
        # Vrátí počet zobrazení článku
        return ArticleView.objects.filter(article=self).count()

    @property
    def get_tags(self):
        # Vrátí všechny tagy přiřazené k článku
        return self.tags.all()
