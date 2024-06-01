from django.db import models

class SingletonModel(models.Model):
    '''
    Abstraktní třída pro implementaci Singleton návrhového vzoru v modelech Django.

    Tato abstraktní třída poskytuje základní funkcionalitu pro implementaci Singletonu.
    Třída vytváří nebo získává jedinou instanci modelu a zajistí,
    že existuje pouze jedna instance tohoto modelu v rámci celé aplikace.
    Atribut abstract indikuje, že se jedná o abstraktní třídu,
    která není mapována na žádnou tabulku v databázi.
    '''

    class Meta:
        abstract = True

    @classmethod
    def singleton(cls):
        '''
        Třídní metoda pro získání jediné instance modelu.

        Tato metoda vrací jedinou instanci modelu a pokud tato instance neexistuje, vytvoří ji.
        Navrací instanci modelau a Bool hodnotu, zda byla vytvořena (True) nebo získána (False).
        '''

        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        '''
        Přetížení metoda save.

        Tato metoda přepisuje standardní metodu pro uložení instance modelu tak,
        aby vždy nastavila primární klíč na hodnotu 1, a tím zajišťuje,
        že v databázi bude pouze jedna instance tohoto modelu.
        '''

        self.pk = 1
        super().save(*args, **kwargs)
