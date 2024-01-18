### Definuje modely (tabulky) pro článek.

from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from PIL import Image
import os
from model_utils import FieldTracker
from django.core.files.storage import default_storage


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



    # Obrázek reprezentující článek - varianta pro článek (800px)
    main_picture_for_article = models.ImageField(upload_to='images/articles/main_picture/')

    # FieldTracker pro sledování změn v profile_image
    main_picture_for_article_tracker = FieldTracker(fields=['main_picture_for_article'])

    # Obrázek reprezentující článek - miniatura (60px)
    main_picture_miniature = models.ImageField(upload_to='images/articles/main_picture/', null=True, blank=True)

    # Obrázek reprezentující článek - náhledová varianta (450px)
    main_picture_preview = models.ImageField(upload_to='images/articles/main_picture/', null=True, blank=True)

    # Obrázek reprezentující článek- vysoké rozlišení (<1920px)
    main_picture_max_size = models.ImageField(upload_to='images/articless/main_picture/', null=True, blank=True)





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

    @property
    def comment_count(self):
        # Vrátí počet komentářů k článku
        return self.comments.count()

    @property
    def get_main_picture_miniature_name(self):
        # Metoda pro generování názvu pro miniaturu obrázku
        return f"{self.slug}_amp_mini_60px.jpg"

    @property
    def get_main_picture_preview_name(self):
        # Metoda pro generování názvu obrázku pro náhledovou velikost
        return f"{self.slug}_amp_preview_450px.jpg"

    @property
    def get_main_picture_for_article_name(self):
        # Metoda pro generování názvu obrázku velikosti pro článek
        return f"{self.slug}_amp_article_800px.jpg"

    @property
    def get_main_picture_max_size_name(self):
        # Metoda pro generování názvu obrázku v nejvyšším rozlišení
        return f"{self.slug}_amp_max_1920px.jpg"

    @classmethod
    def main_picture_path(cls):
        return 'media/images/articles/main_picture/'

    @property
    def get_main_picture_miniature_path(self):
        # Metoda pro generování cesty pro miniaturu obrázku
        main_picture_path = Article.main_picture_path()
        picture_name = self.get_main_picture_miniature_name
        return os.path.join(main_picture_path, picture_name)

    @property
    def get_main_picture_preview_path(self):
        # Metoda pro generování cesty obrázku pro náhledovou velikost
        main_picture_path = Article.main_picture_path()
        picture_name = self.get_main_picture_preview_name
        return os.path.join(main_picture_path, picture_name)

    @property
    def get_main_picture_for_article_path(self):
        # Metoda pro generování cesty obrázku velikosti pro článek
        main_picture_path = Article.main_picture_path()
        picture_name = self.get_main_picture_for_article_name
        return os.path.join(main_picture_path, picture_name)

    @property
    def get_main_picture_max_size_path(self):
        # Metoda pro generování cesty obrázku v nejvyšším rozlišení
        main_picture_path = Article.main_picture_path()
        picture_name = self.get_main_picture_max_size_name
        return os.path.join(main_picture_path, picture_name)


    def save(self, *args, **kwargs):
        print("save")

        if not self.pk:
            # Ověří zda je vytvořené umístění pro soubory, pokud ne, pak ho vytvoří
            os.makedirs(Article.main_picture_path(), exist_ok=True)


        if self.main_picture_for_article_tracker.has_changed('main_picture_for_article'):
            print("if self.main_picture_for_article_tracker.has_changed")

            # Vytvoření kopíí obrázku
            with Image.open(self.main_picture_for_article.path) as img:

                # Pro vysoké rozlišení
                img.thumbnail((1920, 1920))
                img.save(self.get_main_picture_max_size_path, 'JPEG')
                self.main_picture_max_size = self.get_main_picture_max_size_path

                # Pro variantu pro článek
                img.thumbnail((800, 800))
                img.save(self.get_main_picture_for_article_path, 'JPEG')
                # Tato varianta bude přidělena poli až po smazání aktuálně zpracovávaného obrázku

                # Pro náhledovou varianu
                img.thumbnail((450, 450))
                img.save(self.get_main_picture_preview_path, 'JPEG')
                self.main_picture_preview = self.get_main_picture_preview_path

                # Pro miniaturu
                img.thumbnail((60, 60))
                img.save(self.get_main_picture_miniature_path, 'JPEG')
                self.main_picture_miniature = self.get_main_picture_miniature_path


        # Volání původní metody save
        super(Article, self).save(*args, **kwargs)


        # Pokud toto pole neobsahuje defaultní hodnotu
        if self.main_picture_for_article != self.get_main_picture_for_article_path:
            try:
                # Fyzické smazání souboru
                image_path = self.main_picture_for_article.path
                if default_storage.exists(image_path):
                    default_storage.delete(image_path)

                # Nahrazení cesty v databázy
                self.main_picture_for_article = self.get_main_picture_for_article_path

                print("Soubor byl smazán a cesta změněna.")
            except Exception as e:
                print("Chyba po uložení:", str(e))


