from django.db import models
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _
import os
from model_utils import FieldTracker
from django.utils.text import slugify

from utilities.shared.create_thumbnail import create_thumbnail


class ArticleAuthor(models.Model):
    '''
    Model pro autora článku.

    user
    author
    profile_picture
    profile_picture_thumbnail

    [hint]
    profile_picture_tracker
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()
    '''


    # Vztah "one-to-one" s modelem CustomUser (po smazání uživatel autor zůstává)
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True
    )

    # Uživatelské jméno autora článku
    author = models.CharField(
        _("author"),
        max_length=150,
        unique=True
    )

    # Automaický generovaný slug pro URL na základě názvu článku, unikátní
    slug = models.SlugField(
        _("slug"),
        unique=True,
        blank=True
    )

    # Profilový obrázek autora článku
    profile_picture = models.ImageField(
        _("author profile picture"),
        upload_to="images/profile_pictures/authors/"
    )

    # Pole pro miniaturu pro profilový obrázek
    profile_picture_thumbnail = models.ImageField(
        _("profile_picture_thumbnail"),
        upload_to="images/profile_pictures/authors/",
        null=True
    )


    # FieldTracker pro sledování změn v profile_picture
    profile_picture_tracker = FieldTracker(fields=['profile_picture'])


    def __str__(self):
        return self.author

    @property
    def slugify_author(self):
        '''
        Slugifikace emailu

        Všechna znaky malémi písmeny.
        Odstranění z emailové adresy všech znaků, které nejsou vhodné pro použití v URL.
        '''
        return f"{slugify(self.author)}"


    @property
    def profile_picture_name(self):
        '''
        Definice jména profilového obráku

        Přední část je slagifikovaný email uživatele.
        Dodatek tvoří zkrazka pro Author Profile Picture (app) a hodnota velikosti (300).
        '''
        return f"{self.slug}_app_300.jpg"


    @property
    def profile_picture_thumbnail_name(self):
        '''
        Definice jména miniatury profilového obráku

        Přední část je slagifikovaný email.
        Dodatek tvoří zkrazka pro User Profile Picture a hodnota velikosti.
        '''
        return f"{self.slug}_app_150.jpg"


    @property
    def profile_picture_directory(self):
        '''
        Cesta k složce pro profilové obrázky z media root

        (složka profile_pictures obsahuje i složku users pro profilové obrázky uživatele)
        '''
        return f"images/profile_pictures/authors/"

    @property
    def profile_picture_path(self):
        '''
        Cesta k profilovému obrázku z media root

        [hint]
        os.path.join
        '''
        return os.path.join(self.profile_picture_directory, self.profile_picture_name)


    @property
    def profile_picture_thumbnail_path(self):
        '''
        Cesta k miniatuře profilovému obrázku z media root

        [hint]
        os.path.join
        '''
        return os.path.join(self.profile_picture_directory, self.profile_picture_thumbnail_name)


    def save(self, *args, **kwargs):
        '''
        Nastavení metody pro uložení instance.

        Vytvoření uživatelského jména a profilového obrázku, při založení instance.
        Kontrola, zda byl změněn profilový obrázek.
        Pokud byl změně profilový obrázek, bude změněna i jeho miniatura.

        :param args: Poziceové argumenty pro super().save()
        :param kwargs: Klíčové argumenty pro super().save()
        :return: None

        [hint]
        create_default_username()
        create_default_profile_picture()
        create_default_profile_picture()
        creat_thumbnail()
        '''
        new_instance = False
        # Vytvoření uživatelského jména a profilového obrázku, při založení instance.
        if not self.pk:
            self.author = self.user.username
            self.profile_picture = self.user.profile_picture
            self.profile_picture.name = self.profile_picture_name
            self.slug = self.user.slugify_email
            new_instance = True

        # Kontrola, zda byl změněn profilový obrázek.
        change_of_profile_picture = self.profile_picture_tracker.has_changed('profile_picture')

        # Uložení instance
        super().save(*args, **kwargs)

        # Pokud byl změně profilový obrázek, bude změněna i jeho miniatura.
        if change_of_profile_picture:
            create_thumbnail(self)

        # Pokud byla nově vytvořená instance, zapsat id autora do instance uživatele
        if new_instance:
            self.user.linked_author_id = self.pk

    def delete(self, *args, **kwargs):
        # Při smazání instance autora, resetujeme linked_author na None
        self.user.linked_author_id = None
        super().delete(*args, **kwargs)

    @classmethod
    def user_is_author(cls, user):
        '''
        Metoda pro zjištění, zda je určitý uživatel i autorem

        :param cls: Třída (zde ArticleAuthor)
        :param user: Instance uživatele
        :return: True / False

        [hint]
        ArticleAuthor.objects.get(user=user)
        ArticleAuthor.objects.get(user=user)
        '''

        try:
            ArticleAuthor.objects.get(user=user)
            return True

        except ArticleAuthor.DoesNotExist:
            return False
