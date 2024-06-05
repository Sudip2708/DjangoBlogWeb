from django.utils.translation import gettext_lazy as _
from django.db import models
from articles.models.article import Article
from .data.singleton_model import SingletonModel
from tinymce.models import HTMLField


class HomePageLatestArticles(SingletonModel):
    '''
    Database model for the Home Page Latest Articles Section.

    The model inherits from SingletonModel, which is an abstract class defined to create a single instance.

    The model creates the following fields:
    - display_latest_section: Boolean field for representing the display or hiding of the section.
    - latest_title: HTML field for inserting a title to be displayed in this section.
    - latest_description: HTML field for inserting a description to be displayed in this section.
    - latest_article_1: ForeignKey field for selecting the first latest article.
    - latest_article_2: ForeignKey field for selecting the second latest article.
    - latest_article_3: ForeignKey field for selecting the third latest article.

    Model methods:
    - __str__: To get the textual representation of the model (based on the article name field value).
    - get_data: Used to retrieve all the values of this model for rendering on the home page.
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
        Method to retrieve the values of the three latest articles for this model.

        Returns a list of the three latest articles assigned to the model
        or populates the list with new articles if some items are not defined.
        """

        # Retrieve the saved articles in this model
        assigned_articles = [
            self.latest_article_1,
            self.latest_article_2,
            self.latest_article_3
        ]

        # Check if any of the fields does not contain an article id
        if not all(assigned_articles):

            # Retrieve the three latest articles
            latest_articles = list(Article.objects.filter(status='publish').order_by('-created')[:3])

            # Filter out articles already appearing in the model's selection
            for index, article in enumerate(assigned_articles):
                if article in latest_articles:
                    latest_articles = [a for a in latest_articles if a != article]

            # Fill in the missing articles for the model
            for index, article in enumerate(assigned_articles):
                if article is None:
                    assigned_articles[index] = latest_articles.pop(0)

        return assigned_articles


    def get_data(self):
        '''
        Method to retrieve the values of all fields of this model for rendering on the home page.

        Returns a dictionary containing the following information:
        section display, section title, section description, and section articles.
        '''

        return {
            'display_latest_section': self.display_latest_section,
            'latest_title': self.latest_title,
            'latest_description': self.latest_description,
            'articles': self.latest_articles,
        }
