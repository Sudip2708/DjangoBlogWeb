from django.db import models


class DatesAndStatusMixin(models.Model):
    '''
    Mixin pro model Article přidávající pole, která jsou provázaná s datem, a pole pro status.

    Pole vytvořená tímto mixinem:
    - created: Datum vytvoření článku (automaticky vytvořeno při založení instance).
    - updated: Datum poslední úpravy článku (automaticky vytvořeno při uložení instance).
    - published: Datum publikování článku (vytvořeno při změně statusu na 'publish').
    - status: Pole určující status článku, které má tyto tři volby:
        - drafted: Pro nově vytvořené články a články, které se přepracovávají.
        - publish: Pro hotové články, které jsou určené ke zveřejnění.
        - archive: Pro hotové články, které nechceme, aby byly veřejně přístupné.

    Mixin má definovanou vnitřní třídu Meta pro nastavení abstraktního chování.
    (Samostatně nevytváří ID a tabulku v databázi.)
    '''

    created = models.DateTimeField(
        verbose_name='Article Created Date',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name="Article Updated Date",
        auto_now=True,
    )

    published = models.DateTimeField(
        verbose_name='Article Published Date',
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name='Article Status',
        max_length=20,
        choices=[('drafted', 'Drafted'), ('publish', 'Publish'), ('archive', 'Archive')],
        blank=True,
    )

    class Meta:
        abstract = True