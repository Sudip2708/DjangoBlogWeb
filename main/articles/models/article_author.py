### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# get_user_model(): funkce, která vrací třídu modelu uživatele použitou ve vaší aplikaci


class ArticleAuthor(models.Model):
    '''
    Model pro databázovou tabulku pro autora příspěvku

    Nápověda:
    [definice pole]
    models.OneToOneField(): pole, které vytváří vztah "jeden k jednomu" mezi dvěma modely
    models.ImageField(): pole, pro ukládání obrázku
    [parametry]
    User: funkce, která vrací třídu modelu uživatele použitou ve vaší aplikaci
    on_delete=models.CASCADE: parametr, který definuje chování při smazání záznamu odkazovaného modelu (smaže spojený záznam při smazání odkazovaného záznamu)
    '''
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.author.username