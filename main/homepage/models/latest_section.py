from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article
from .data.singleton_model import SingletonModel
from tinymce.models import HTMLField


class HomePageLatestArticles(SingletonModel):
    '''
    Databázový model pro Home Page Latest Articles Section.

    Model dědí ze SingletonModel, což je abstraktní třída definovaná pro vytvoření jediné instance.

    Model vytváří následující pole:
    - display_latest_section: Boolean pole pro hodnotu reprezentující zobrazení nebo skrytí sekce.
    - latest_title: HTML pole pro vložení nadpisu, který bude zobrazen v této sekci.
    - latest_description: HTML pole pro vložení popisu, který bude zobrazen v této sekci.
    - latest_article_1: ForeignKey pole pro výběr prvního nejnovějšího článku.
    - latest_article_2: ForeignKey pole pro výběr druhého nejnovějšího článku.
    - latest_article_3: ForeignKey pole pro výběr třetího nejnovějšího článku.

    Metody modelu:
    - __str__: Pro získání textové reprezentace modelu (dle hodnoty pole pro název článku).
    - get_data: Slouží k získání všech hodnot tohoto modelu pro vykreslení na domácí stránce.
    '''


    display_latest_section = models.BooleanField(
        _('Display Latest Section'),
        default=True,
    )

    latest_title = HTMLField(
        _('Latest Articles Title'),
        null=True, blank=True
    )

    latest_description = HTMLField(
        _('Latest Articles Description'),
        null=True, blank=True
    )

    latest_article_1 = models.ForeignKey(
        Article,
        related_name='latest_article_1',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Latest Article 1')
    )

    latest_article_2 = models.ForeignKey(
        Article,
        related_name='latest_article_2',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Latest Article 2')
    )

    latest_article_3 = models.ForeignKey(
        Article,
        related_name='latest_article_3',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_('Latest Article 3')
    )

    def __str__(self):
        return "Homepage Latest Articles Configuration"

    @property
    def latest_articles(self):
        """
        Metoda, která slouží k získání hodnot tří nejnovějších článků pro tento model.

        Vrátí seznam tří nejnovějších článků přiřazených k modelu
        nebo doplní seznam novými články, pokud některé položky nejsou definovány.
        """

        # Načtení uložených článků v tomto modelu
        assigned_articles = [
            self.latest_article_1,
            self.latest_article_2,
            self.latest_article_3
        ]

        # Kontrola, zda některé z polí neobsahuje id článku
        if not all(assigned_articles):

            # Načtení tří nejnovějších článků
            latest_articles = list(Article.objects.filter(status='publish').order_by('-created')[:3])

            # Odfiltrování článků, které se již vyskytují v nabídce modelu
            for index, article in enumerate(assigned_articles):
                if article in latest_articles:
                    latest_articles = [a for a in latest_articles if a != article]

            # Doplnění chybějících článků modelu
            for index, article in enumerate(assigned_articles):
                if article is None:
                    assigned_articles[index] = latest_articles.pop(0)

        return assigned_articles


    def get_data(self):
        '''
        Metoda, která slouží k získání hodnot všech polí tohoto modelu pro vykreslení na domácí stránce.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, nadpis, popis a články sekce.
        '''

        return {
            'display_latest_section': self.display_latest_section,
            'latest_title': self.latest_title,
            'latest_description': self.latest_description,
            'articles': self.latest_articles,
        }