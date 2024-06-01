from django.db import models

from users.models.custom_user import CustomUser

from .article_author_data.profile_picture_processing import profile_picture_processing


class ArticleAuthor(models.Model):
    '''
    Model reprezentující autora článku.

    Tento model uchovává informace o uživateli, který je autorem článku
    a obsahuje následující pole:
    - linked_user: Pole propojující účet autora s uživatelským účtem pomocí vztahu "one-to-one" s modelem CustomUser.
    - name: Pole pro uživatelské jméno autora, které se zobrazuje v souvislosti s jeho články.
    - slug: Pole pro unikátní "slug", který slouží pro vytváření adresy URL odvozené z jeho jména.
    - profile_picture: Pole pro profilový obrázek autora.
    - profile_picture_thumbnail: Pole pro miniaturu profilového obrázku.

    Model definuje tyto atributy pro profilové obrázky:
    - default_picture: Cesta z Media k defaultnímu obrázku (použit při vytvoření instance bez udání obrázku).
    - upload_path: Cesta z Media pro uložení všech velikostních variant hlavního obrázku.
    - new_picture: Boolean hodnota, zda došlo k novému nahrání obrázku (nastavuje se ve formuláři
        po obdržení nového souboru pro obrázek a je zachytávána v post_save signálu pro zpracování obrázku).

    Metody modelu:
    - __str__: Získání textové reprezentace modelu (dle hodnoty pole pro jméno autora).
    - profile_picture_processing: Metoda pro úpravu profilového obrázku.

    Model má na sebe navázaných několik pre_save, post_save, pre_delete a post_delete signálů,
    zpracovávající její obsah.
    '''

    linked_user = models.OneToOneField(
        CustomUser,
        verbose_name='Linked User',
        related_name='linked_author',
        null=True,
        on_delete=models.SET_NULL,
    )

    name = models.CharField(
        verbose_name='Author Name',
        blank=True,
        unique=True,
        max_length=50,
    )

    slug = models.SlugField(
        verbose_name='Author Slug',
        blank=True,
        unique=True,
    )

    default_picture = 'images/profile_pictures/default.jpg'
    upload_path = 'images/profile_pictures/authors/'
    new_picture = False

    profile_picture = models.ImageField(
        verbose_name='Profile Picture',
        default=default_picture,
        upload_to=upload_path,
    )

    profile_picture_thumbnail = models.ImageField(
        verbose_name='Profile Picture Thumbnail',
        default=default_picture,
        upload_to=upload_path,
    )

    def __str__(self):
        return self.name

    def profile_picture_processing(self):
        ''' Metoda pro úpravu profilového obrázku (a vytvoření miniatury). '''
        return profile_picture_processing(self)