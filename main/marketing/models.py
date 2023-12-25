### Definuje modely (tabulky) pro aplikaci.


from django.db import models
'''
[from]
django.db: balíček, který poskytuje nástroje pro definici a práci s modely databáze
[import]
models: modul, který obsahuje různé třídy a pole k definování struktury databáze
'''


class Signup(models.Model):
    '''
    Model pro databázovou tabulku pro email na odebírání novinek

    Nápověda:
    [pole]
    models.EmailField(): pole, pro ukládání emailu
    models.DateTimeField(): pole, které představuje datum a čas
    [parametry]
    auto_now_add=True:
    '''
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
