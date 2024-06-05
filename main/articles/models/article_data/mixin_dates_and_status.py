from django.db import models


class DatesAndStatusMixin(models.Model):
    '''
    Mixin for the Article model adding fields related to dates and status.

    Fields created by this mixin:
    - created: The date the article was created (automatically generated when the instance is created).
    - updated: The date of the last update to the article (automatically updated when the instance is saved).
    - published: The date the article was published (set when the status changes to 'publish').
    - status: Field indicating the status of the article, with three options:
        - drafted: For newly created articles and articles being revised.
        - publish: For finished articles intended for publication.
        - archive: For finished articles not intended for public access.

    The mixin defines an inner Meta class to set abstract behavior.
    (It does not create its own ID or table in the database.)
    '''

    created = models.DateTimeField(
        verbose_name='Article Created Date',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name="Article Updated Date",
        auto_now=True,
    )

    published = models.DateTimeField(
        verbose_name='Article Published Date',
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name='Article Status',
        max_length=20,
        choices=[('drafted', 'Drafted'), ('publish', 'Publish'), ('archive', 'Archive')],
        blank=True,
    )

    class Meta:
        abstract = True
