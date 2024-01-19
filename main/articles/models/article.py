from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from model_utils import FieldTracker

from .article_author import ArticleAuthor
from .article_category import ArticleCategory
from .article_mixins.article_base_methods_mixin import ArticleBaseMethodsMixin
from .article_mixins.article_databases_property_mixin import ArticleDatabasesPropertyMixin
from .article_mixins.article_images_property_mixin import ArticleImagesPropertyMixin
from .article_mixins.article_images_processing_mixin import ArticleImagesProcessingMixin


class Article(models.Model,
              ArticleBaseMethodsMixin,
              ArticleDatabasesPropertyMixin,
              ArticleImagesPropertyMixin,
              ArticleImagesProcessingMixin):
    """
    Model reprezentující článek.

    Attributes:
        author: Cizí klíč na autora článku.
        title: Název článku, omezený na 100 znaků.
        slug: Automaický generovaný slug pro URL na základě názvu článku, unikátní.
        overview: Krátký popis článku.
        content: Obsah článku v HTML formátu.
        main_picture_for_article: Obrázek reprezentující článek.
        main_picture_miniature: Miniatura obrázku reprezentujícího článek.
        main_picture_preview: Náhledová varianta obrázku reprezentujícího článek.
        main_picture_max_size: Obrázek v nejvyšším rozlišení.
        created: Datum vytvoření článku.
        updated: Datum poslední aktualizace článku.
        tags: Správce pro práci s tagy.
        categories: Množina kategorií, ke kterým článek patří.
        comment_count: Počet komentářů k článku.
        featured: Příznak, zda je článek označený jako "featured".
        previous_article: Odkaz na předchozí článek.
        next_article: Odkaz na následující článek.
    """

    # Cizí klíč na autora článku
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE)

    # Název článku, omezený na 100 znaků
    title = models.CharField(_("article_title"), max_length=100)

    # Automaický generovaný slug pro URL na základě názvu článku, unikátní
    slug = AutoSlugField(populate_from='title', unique=True)

    # Krátký popis článku
    overview = models.TextField(_("article_overview"))

    # Obsah článku v HTML formátu
    content = HTMLField(_("article_main_content"))

    # Obrázek reprezentující článek - varianta pro článek (800px)
    main_picture_for_article = models.ImageField(_("article_main_picture"), upload_to='images/articles/main_picture/')

    # FieldTracker pro sledování změn v main_picture_for_article
    main_picture_for_article_tracker = FieldTracker(fields=['main_picture_for_article'])

    # Obrázek reprezentující článek - miniatura (60px)
    main_picture_miniature = models.ImageField(upload_to='images/articles/main_picture/', null=True, blank=True)

    # Obrázek reprezentující článek - náhledová varianta (450px)
    main_picture_preview = models.ImageField(upload_to='images/articles/main_picture/', null=True, blank=True)

    # Obrázek reprezentující článek- vysoké rozlišení (<1920px)
    main_picture_max_size = models.ImageField(upload_to='images/articles/main_picture/', null=True, blank=True)

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
