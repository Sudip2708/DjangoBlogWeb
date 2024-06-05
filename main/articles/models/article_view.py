from django.db import models

from users.models.custom_user import CustomUser


class ArticleView(models.Model):
    '''
    Model representing a view of an article.

    This model stores information about the view of an article, including the user who viewed the article,
    and includes the following fields:
    - article: ForeignKey field referencing the article that was viewed.
    - user: ForeignKey field referencing the user who viewed the article.
        (This field may be empty for unauthenticated users).
    - ip_address: Field for the user's IP address, used to differentiate unique views for unauthenticated users.
    - created: Field for the date and time the instance (article view) was created.

    Model methods:
    - __str__: Obtains the textual representation of the model (based on the username).
    - record_view: Records a view of the article.
    - get_view_count: Returns the count of views for the article.
    '''

    article = models.ForeignKey(
        'Article',
        verbose_name='View Article',
        related_name='view_count',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        CustomUser,
        verbose_name='View User',
        related_name='article_view_count',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    ip_address = models.GenericIPAddressField(
        verbose_name='IP Address',
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name='View Created',
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username if self.user else "Anonymous"

    @staticmethod
    def record_view(article, user, ip_address):
        '''
        Static method to record a view of the article.

        Creates a new instance of ArticleView with the relevant parameters.
        '''
        ArticleView.objects.create(
            article=article,
            user=user if user.is_authenticated else None,
            ip_address=ip_address
        )

    @staticmethod
    def get_view_count(article):
        '''
        Static method to retrieve the count of views for the article.

        Returns the count of records in ArticleView for the given article.
        '''
        return ArticleView.objects.filter(article=article).count()
