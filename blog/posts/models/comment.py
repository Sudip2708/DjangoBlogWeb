### Definuje modely (tabulky) pro aplikaci.

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# get_user_model(): funkce, která vrací třídu modelu uživatele použitou ve vaší aplikaci


class Comment(models.Model):
    '''
    Tento kód zpracovává formulář s komentářem k příspěvku (post).
    Kód přijímá data z formuláře pomocí HTTP POST požadavku, ověřuje, zda jsou data platná, a pokud ano, uloží komentář do databáze a přesměruje uživatele na detail příspěvku.

    Nápověda:
    [definice pole]
    models.ForeignKey(): pole, které vytváří vztah k jinému modelu v databázi (cizí klíč)
    DateTimeField(): pole, které představuje datum a čas
    models.TextField(): pole, které představuje delší textový řetězec bez omezení délky
    [parametry]
    User: třída, která reprezentuje uživatele aplikace
    on_delete=models.CASCADE: parametr, který znamená, že pokud je uživatelský účet (nebo příspěvek) smazán, všechny komentáře, které jsou s ním spojeny, budou také smazány
    auto_now_add=True: parametr, který automaticky nastavuje hodnotu na aktuální datum a čas při vytváření instance modelu
    Post: třída, která reprezentuje obsah, ke kterému mohou být přidány komentáře
    related_name='comments': volitelný parametr, který umožňuje pojmenovat relaci z druhé strany. V tomto případě, když máte instanci Post, můžete přistupovat k přidruženým komentářům pomocí jména "comments". Například, pokud máte instanci post, můžete získat všechny komentáře k tomuto příspěvku pomocí výrazu post.comments.all()
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username