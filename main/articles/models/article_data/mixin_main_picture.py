from django.db import models
import os

from .main_picture_processing import main_picture_processing


class MainPictureMixin(models.Model):
    '''
    Mixin pro model Article přidávající pole pro uložení různých velikostních variant hlavního obrázku.

    Mixin definuje tyto atributy:
    - default_picture: Cesta z Media k defaultnímu obrázku (použit při vytvoření instance bez udání obrázku).
    - upload_path: Cesta z Media pro uložení všech velikostních variant hlavního obrázku.
    - new_picture: Boolean hodnota, zda došlo k novému nahrání obrázku (nastavuje se ve formuláři
        po obdržení nového souboru pro obrázek a je zachytávána v post_save signálu pro zpracování obrázku).

    Pole vytvořená tímto mixinem:
    - main_picture_max_size: Největší velikost obrázku pro samotné zobrazení obrázku přes celou obrazovku.
        (maximální rozměr: 1920px / 1080px, minimální rozměr: 800px / 800px)
    - main_picture_for_article: Střední velikost obrázku pro použití na stránce článku.
        (maximální šířka: 440px, minimální šířka: 800px)
    - main_picture_preview: Menší velikost obrázku pro zobrazení na stránce s výpisem článků.
        (oříznutí na poměr 4:3 a zmenšení velikosti na 440px / 330px)
    - main_picture_thumbnail: Miniatura použitá pro odkaz článku.
        (oříznutí na čtvercový formát a zmenšení velikosti na 150px)

    Mixin má definovanou vnitřní třídu Meta pro nastavení abstraktního chování.
    (Samostatně nevytváří ID a tabulku v databázi.)

    Mixin obsahuje metodu 'picture_processing',
    která vytváří z nahraného obrázku jednotlivé jeho velikostní varianty.
    '''

    default_picture = 'images/articles/no-image.jpg'
    upload_path = 'images/articles/main_picture/'
    new_picture = False

    main_picture_max_size = models.ImageField(
        'Article Main Picture Max-Size',
        default=default_picture,
        upload_to=upload_path,
    )

    main_picture_for_article = models.ImageField(
        'Article Main Picture',
        default=default_picture,
        upload_to=upload_path,
    )

    main_picture_preview = models.ImageField(
        'Article Main Picture Preview',
        default=default_picture,
        upload_to=upload_path,
    )

    main_picture_thumbnail = models.ImageField(
        'Article Main Picture Miniature',
        default=default_picture,
        upload_to=upload_path,
    )

    class Meta:
        abstract = True

    def main_picture_processing(self):
        ''' Metoda pro vytvoření velikostních variant hlavního obrázku článku. '''
        return main_picture_processing(self)
