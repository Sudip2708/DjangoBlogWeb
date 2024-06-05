from django.db import models

from users.models.custom_user import CustomUser


class ArticleComment(models.Model):
    '''
    Model representing a comment on an article.

    This model stores information about the comment that a user added to an article
    and includes the following fields:
    - article: ForeignKey field referencing the article to which the comment is attached.
    - user: ForeignKey field referencing the user who created the comment.
    - content: Field for the content of the comment.
    - created: Field for the date and time the comment was created.

    Model methods:
    - __str__: Obtains the textual representation of the model (based on the username).
    '''

    article = models.ForeignKey(
        'Article',
        verbose_name='Comment Article',
        related_name='comments',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        CustomUser,
        verbose_name='Comment User',
        related_name='user_comments',
        null=True,
        on_delete=models.SET_NULL,
    )

    content = models.TextField(
        verbose_name='Comment Content',
    )

    created = models.DateTimeField(
        verbose_name='Comment Created',
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username
