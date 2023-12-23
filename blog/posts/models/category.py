### Definuje modely (tabulky) pro aplikaci.

from django.db import models

class Category(models.Model):
    '''
    Model pro databázovou tabulku pro kategorie příspěvku

    Nápověda:
    [definice pole]
    models.CharField(): pole, které představuje textový řetězec v databázi
    [parametry]
    max_length: parametr, který určuje maximální délku textového řetězce (počet znaků)
    '''
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title