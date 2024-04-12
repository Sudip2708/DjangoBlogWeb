from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article
from .singleton_model import SingletonModel
from tinymce.models import HTMLField


class HomePageLatestArticles(SingletonModel):
    '''
    Databázový model pro Home Page Latest Articles Section

    Obsahuje pole pro nastavení zobrazení sekce, nadpisu, popisu a článků této sekce.
    Metoda __str__ definuje textovou reprezentaci instance tohoto modelu.
    Metoda get_divider_settings slouží k získání všech hodnot tohoto modelu.
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
        Vlastnost, která slouží k získání hodnot tří nejnovějších článků pro tento model.

        Vrátí seznam tří nejnovějších článků přiřazených k modelu
        nebo doplní seznam novými články, pokud některé položky nejsou definovány.

        :return: Seznam tří nejnovějších přiřazených článků nebo seznam nových článků.
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

    @property
    def get_latest_settings(self):
        '''
        Vlastnost, která slouží k získání hodnot všech polí tohoto modelu.

        Vrací slovník obsahující následující informace:
        zobrazení sekce, nadpis, popis a články sekce.
        '''

        return {
            'display_latest_section': self.display_latest_section,
            'latest_title': self.latest_title,
            'latest_description': self.latest_description,
            'articles': self.latest_articles,
        }