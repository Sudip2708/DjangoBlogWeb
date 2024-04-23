print('### 12 main/articles/models/article.py')

import os
from django.urls import reverse
from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from model_utils import FieldTracker
from django.utils import timezone

from .article_author import ArticleAuthor
from .article_category import ArticleCategory
from .article_view import ArticleView
from articles.utilities.create_other_sizes_of_main_picture import create_other_sizes_of_main_picture
from articles.schema_methods.index_article_content import index_article_content


class Article(models.Model):
    '''
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
        category: Množina kategorií, ke kterým článek patří.
        comment_count: Počet komentářů k článku.
        featured: Příznak, zda je článek označený jako 'featured'.
        previous_article: Odkaz na předchozí článek.
        next_article: Odkaz na následující článek.
    '''

    # Cizí klíč na autora článku
    author = models.ForeignKey(
        ArticleAuthor,
        on_delete=models.CASCADE,
        verbose_name=_('Article Author')
    )

    # Název článku, omezený na 100 znaků
    title = models.CharField(
        _('Article Title'),
        max_length=100
    )

    # Automaický generovaný slug pro URL na základě názvu článku, unikátní
    slug = AutoSlugField(
        _('Article Slug'),
        populate_from='title',
        unique=True
    )

    # Krátký popis článku
    overview = models.TextField(
        _('Article overview'),
        null=True, blank=True
    )

    # Obsah článku v HTML formátu
    content = HTMLField(
        _('Article main_content'),
        null=True, blank=True
    )

    # Obrázek reprezentující článek- vysoké rozlišení (<1920px)
    main_picture_max_size = models.ImageField(
        _('Article Main Picture Max-Size'),
        upload_to='images/articles/main_picture/',
        null=True, blank=True
    )

    # FieldTracker pro sledování změn v profile_image
    main_picture_max_size_tracker = FieldTracker(
        fields=['main_picture_max_size']
    )

    # Obrázek reprezentující článek - varianta pro článek (800px)
    main_picture_for_article = models.ImageField(
        _('Article Main Picture'),
        upload_to='images/articles/main_picture/',
        null=True, blank=True
    )

    # Obrázek reprezentující článek - náhledová varianta (520px)
    main_picture_preview = models.ImageField(
        _('Article Main Picture Preview'),
        upload_to='images/articles/main_picture/',
        null=True, blank=True
    )

    # Obrázek reprezentující článek - miniatura (150px)
    main_picture_miniature = models.ImageField(
        _('Article Main Picture Miniature'),
        upload_to='images/articles/main_picture/',
        null=True, blank=True
    )

    # Datum vytvoření článku
    created = models.DateTimeField(
        _('Article Created Date '),
        auto_now_add=True
    )

    # Datum poslední aktualizace článku
    updated = models.DateTimeField(
        _('Article Updated Date '),
        auto_now=True
    )

    # Datum zveřejnění článku
    published = models.DateTimeField(
        _('Article Published Date'),
        null=True, blank=True
    )


    # Správce pro práci s tagy
    tags = TaggableManager(
        _('Article Tag'),
        blank=True
    )

    # Množina kategorií, ke kterým článek patří
    category = models.ForeignKey(
        ArticleCategory,
        default=ArticleCategory.get_default_category_id,
        on_delete=models.SET_DEFAULT,
        related_name='article_category',
        verbose_name=_('Article Category')
    )

    # Počet komentářů k článku
    comment_count = models.PositiveIntegerField(
        _('Article Comment Count'),
        default=0
    )

    # Status článku
    status = models.CharField(
        _('Article Status'),
        max_length=20,
        choices=[('drafted', 'Drafted'), ('publish', 'Publish'), ('archive', 'Archive')],
        default='draft'
    )


    # Příznak, zda je článek označený jako 'featured' pro hlavní stránku
    featured = models.BooleanField(
        _('Featured Article'),
        default=False
    )

    # Odkazy na předchozí a následující článek
    previous_article = models.ForeignKey(
        'self',
        related_name='previous',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Previous Article')
    )

    next_article = models.ForeignKey(
        'self',
        related_name='next',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Next Article')
    )

    class Meta:
        # Index pro rychlejší vyhledávání podle slugu
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        '''
        Vrátí textovou reprezentaci instance (pro administrační rozhraní a výpisy)
        '''
        return self.title

    def get_absolute_url(self):
        '''
        Vrátí absolutní URL pro zobrazení detailu článku.
        '''
        return reverse('article-detail', kwargs={'slug': self.slug})


    def get_update_url(self):
        '''
        Vrátí URL pro aktualizaci článku.
        '''
        return reverse('article-update', kwargs={'slug': self.slug})


    def get_delete_url(self):
        '''
        Vrátí URL pro smazání článku.
        '''
        return reverse('article-delete', kwargs={'slug': self.slug})


    @property
    def get_comments(self):
        '''
        Vrátí všechny komentáře k článku, seřazené sestupně podle data vytvoření.
        '''
        return self.comments.all().order_by('-created')


    @property
    def view_count(self):
        '''
        Vrátí počet zobrazení článku.
        '''
        return ArticleView.objects.filter(article=self).count()


    @property
    def get_tags(self):
        '''
        Vrátí všechny tagy přiřazené k článku.
        '''
        return self.tags.all()


    @property
    def comment_count(self):
        '''
        Vrátí počet komentářů k článku.
        '''
        return self.comments.count()


    @classmethod
    def main_picture_path(cls):
        '''
        Vrátí cestu k hlavní složce pro obrázky článků.
        '''
        return 'images/articles/main_picture/'


    @property
    def main_picture_miniature_path(self):
        '''
        Vrátí cestu pro miniaturu obrázku.
        '''
        main_picture_path = Article.main_picture_path()
        picture_name = f'{self.slug}_amp_mini_150px.jpg'
        return os.path.join(main_picture_path, picture_name)


    @property
    def main_picture_preview_path(self):
        '''
        Vrátí cestu pro náhledovou velikost obrázku.
        '''
        main_picture_path = Article.main_picture_path()
        picture_name = f'{self.slug}_amp_preview_450px.jpg'
        return os.path.join(main_picture_path, picture_name)


    @property
    def main_picture_for_article_path(self):
        '''
        Vrátí cestu obrázku velikosti pro článek.
        '''
        main_picture_path = Article.main_picture_path()
        picture_name = f'{self.slug}_amp_article_800px.jpg'
        return os.path.join(main_picture_path, picture_name)


    @property
    def main_picture_max_size_name(self):
        '''
        Vrátí jméno pro obrázek v nejvyšším rozlišení.
        '''
        return f'{self.slug}_amp_max_1920px.jpg'

    @property
    def main_picture_max_size_path(self):
        '''
        Vrátí cestu pro obrázek v nejvyšším rozlišení.
        '''
        main_picture_path = Article.main_picture_path()
        picture_name = f'{self.slug}_amp_max_1920px.jpg'
        return os.path.join(main_picture_path, picture_name)


    def save(self, *args, **kwargs):

        # Akce spuštěné při založení instance
        if not self.pk:
            # Ověří zda je vytvořené umístění pro soubory, pokud ne, pak ho vytvoří
            os.makedirs(Article.main_picture_path(), exist_ok=True)

        # Indexace článku
        index_article_content(self)

        # Kontrola, zda byl změněn hlavní obrázek.
        change_of_max_size_picture = self.main_picture_max_size_tracker.has_changed('main_picture_max_size')

        # Kontrola zda je článek publikovaný a má i vyplněný datum publikace
        if self.status == 'publish' and not self.publish_date:
            self.publish_date = timezone.now()
        elif self.status != 'publish' and self.publish_date:
            self.publish_date = None

        # Uložení instance
        super().save(*args, **kwargs)

        # Pokud byl změně profilový obrázek, bude změněna i jeho miniatura.
        if change_of_max_size_picture:
            create_other_sizes_of_main_picture(self)


