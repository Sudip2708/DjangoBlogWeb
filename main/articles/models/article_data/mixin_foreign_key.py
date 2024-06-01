from django.db import models

from taggit.managers import TaggableManager

from ..article_category import ArticleCategory
from ..article_author import ArticleAuthor


class ForeignKeyMixin(models.Model):
    '''
    Mixin pro model Article přidávající pole, která jsou provázaná s dalšími modely.

    Pole vytvořená tímto mixinem:
    - author: Cizí klíč na autora článku.
    - category: Cizí klíč na kategorii, do které článek patří.
    - tags: Propojení na modul Taggit pro správu tagů.
    - previous_article: Cizí klíč na vlastní třídu pro definici předcházejícího článku.
    - next_article: Cizí klíč na vlastní třídu pro definici následujícího článku.

    Mixin má definovanou vnitřní třídu Meta pro nastavení abstraktního chování.
    (Samostatně nevytváří ID a tabulku v databázi.)

    Mixin přidává atribut:
    self.tags_to_delete: seznam pro kontrolu smazaných tagů
    (je plněn metodou clean ve formuláři a mazán v post_save signálu handle_delete_unused_tags_post_save).
    '''

    author = models.ForeignKey(
        ArticleAuthor,
        verbose_name='Article Author',
        related_name='linked_articles',
        null=True,
        on_delete=models.SET_NULL,
    )

    category = models.ForeignKey(
        ArticleCategory,
        verbose_name='Article Category',
        related_name='linked_articles',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,

    )

    tags = TaggableManager(
        verbose_name='Article Tag',
        blank=True
    )

    tags_to_delete = []

    previous_article = models.ForeignKey(
        'self',
        verbose_name='Previous Article',
        related_name='previous',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    next_article = models.ForeignKey(
        'self',
        verbose_name='Next Article',
        related_name='next',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True





