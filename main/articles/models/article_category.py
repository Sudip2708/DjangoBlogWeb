from django.db import models


class ArticleCategory(models.Model):
    '''
    Model representing an article category.

    This model stores information about the category of an article and includes the following fields:
    - name: Field for the category name, limited to 50 characters and unique.
    - slug: Field for a unique "slug" used to create a URL derived from the category name.
    - count: Field for the count of occurrences, storing the number of articles in this category.

    Model methods:
    - __str__: Obtains the textual representation of the model (based on the category name field value).
    '''

    name = models.CharField(
        verbose_name='Category Name',
        unique=True,
        max_length=50,
    )

    slug = models.SlugField(
        verbose_name='Category Slug',
        blank=True,
        unique=True,
    )

    count = models.IntegerField(
        verbose_name='Category Count',
        default=0
    )

    def __str__(self):
        return self.name
