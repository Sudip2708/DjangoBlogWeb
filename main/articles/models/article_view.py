### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# get_user_model(): funkce, která vrací třídu modelu uživatele použitou ve vaší aplikaci



class ArticleView(models.Model):
    '''
    Třída pro počítání zhlédnutí příspěvků
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username