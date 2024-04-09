from django.db import models

class SingletonModel(models.Model):
    '''
    Abstraktní třída pro implementaci Singleton návrhového vzoru v modelech Django.

    Tato abstraktní třída poskytuje základní funkcionalitu pro implementaci Singletonu,
    což znamená, že vytváří nebo získává jedinou instanci modelu a zajistí, že existuje pouze jedna instance
    tohoto modelu v rámci celé aplikace.

    Attributes:
        abstract (bool): Bool hodnota, která indikuje, že se jedná o abstraktní třídu,
            která nemá odpovídající tabulku v databázi.
    '''

    class Meta:
        abstract = True

    @classmethod
    def singleton(cls):
        '''
        Metoda třídy pro získání jediné instance modelu.

        Tato metoda vrací jedinou instanci modelu a pokud tato instance neexistuje,
        vytvoří ji.

        Returns:
            instance: Jedna instance modelu.
            created (bool): Bool hodnota, která indikuje, zda byla instance vytvořena (True) nebo získána (False).
        '''
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        '''
        Metoda pro uložení instance modelu.

        Tato metoda přepisuje standardní metodu pro uložení instance modelu
        tak, aby vždy nastavila primární klíč na hodnotu 1, což zajišťuje, že v databázi bude
        pouze jedna instance tohoto modelu.

        Args:
            *args: Volitelné pozicové argumenty.
            **kwargs: Volitelné klíčové argumenty.
        '''
        self.pk = 1
        super().save(*args, **kwargs)
