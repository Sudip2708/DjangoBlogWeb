from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField

from .article_data.mixin_main_picture import MainPictureMixin
from .article_data.mixin_dates_and_status import DatesAndStatusMixin
from .article_data.mixin_foreign_key import ForeignKeyMixin


class Article(MainPictureMixin, DatesAndStatusMixin, ForeignKeyMixin, models.Model):
    '''
    Model pro data článku.

    Model dědí ze základní třídy models.Model a přidává následující mixiny:
    - MainPictureMixin: Mixin obsahující pole a metody pro zpracování obrázku.
    - DatesAndStatusMixin: Mixin přidávající pole a metody pro zpracování dat a statusu.
    - ForeignKeyMixin: Mixin přidávající pole, která jsou navázána na jiné modely.

    V této části model vytváří následující pole:
    - title: Pole pro nadpis článku.
    - slug: Pole pro slug nadpisu článku (použité pro vytváření URL).
    - overview: Pole pro úvod k článku (v náhledu článku je vidět pouze tato část).
    - content: Pole pro obsah článku, který je tvořen HTML obsahem modulu TinyMCE.

    Z mixinů pak dědí tato pole:
    DatesAndStatusMixin:
    - created: Datum vytvoření článku.
    - updated: Datum poslední úpravy článku.
    - published: Datum publikování článku.
    - status: Pole určující status článku.

    ForeignKeyMixin:
    - author: Cizí klíč na autora článku.
    - category: Cizí klíč na kategorii, do které článek patří.
    - tags: Propojení na modul Taggit pro správu tagů.
    - previous_article: Cizí klíč na vlastní třídu pro definici předcházejícího článku.
    - next_article: Cizí klíč na vlastní třídu pro definici následujícího článku.

    MainPictureMixin:
    - main_picture_max_size: Největší velikost obrázku pro samotné zobrazení obrázku přes celou obrazovku.
    - main_picture_for_article: Střední velikost obrázku pro použití na stránce článku.
    - main_picture_preview: Menší velikost obrázku pro zobrazení na stránce s výpisem článků.
    - main_picture_thumbnail: Miniatura použitá pro odkaz článku.

    Metody modelu přidané v této části:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - get_absolute_url: Pro získání URL adresy k článku.

    Metody získané z mixinů:
    - picture_processing: Metoda pro zpracování hlavního obrázku a uložení jeho různých velikostí.

    Model má na sebe navázaných několik pre_save, post_save, pre_delete a post_delete signálů,
    zpracovávající její obsah.
    '''

    title = models.CharField(
        verbose_name='Article Title',
        blank=True,
        unique=True,
        max_length=100
    )

    slug = models.SlugField(
        verbose_name='Article Slug',
        blank=True,
        unique=True,
    )

    overview = models.TextField(
        verbose_name='Article Overview',
        blank=True,
        null=True,
    )

    content = HTMLField(
        verbose_name='Article Content',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ''' Vrátí absolutní URL pro zobrazení detailu článku. '''
        return reverse('article-detail', kwargs={'slug': self.slug})







