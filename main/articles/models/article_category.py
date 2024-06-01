from django.db import models


class ArticleCategory(models.Model):
    '''
    Model reprezentující kategorii článku.

    Tento model uchovává informace o kategorii článku a obsahuje následující pole:
    - name: Pole pro název kategorie, které je omezeno na 50 znaků a je unikátní.
    - slug: Pole pro unikátní "slug", který slouží pro vytváření adresy URL odvozené z názvu kategorie.
    - count: Pole pro počet výskytů, které uchovává počet článků v této kategorii.

    Metody modelu:
    - __str__: Získání textové reprezentace modelu (dle hodnoty pole pro jméno kategorie).
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
