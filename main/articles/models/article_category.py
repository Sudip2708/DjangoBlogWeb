### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from autoslug import AutoSlugField

class ArticleCategory(models.Model):
    '''
    Model pro databázovou tabulku pro kategorie příspěvku

    Nápověda:
    [definice pole]
    models.CharField(): pole, které představuje textový řetězec v databázi
    [parametry]
    max_length: parametr, který určuje maximální délku textového řetězce (počet znaků)
    '''
    title = models.CharField(max_length=25)
    slug = AutoSlugField(populate_from='title', unique=True)


    def __str__(self):
        return self.title