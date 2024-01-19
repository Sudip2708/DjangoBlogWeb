
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from model_utils import FieldTracker
import os

from .models_utils.managers import CustomUserManager
from .models_utils.create_username import create_username
from .models_utils.create_profile_picture import create_profile_picture



class CustomUser(AbstractUser):

    # Pole pro uživatelské jméno
    username = models.CharField(_("username"), max_length=150, unique=True)

    # Pole pro email
    email = models.EmailField(_("email_address"), unique=True)

    # Pole pro profilový obrázek
    profile_picture = models.ImageField(_("profile_picture"), upload_to="images/profile_pictures/users/", null=True)

    # FieldTracker pro sledování změn v profile_picture
    profile_picture_tracker = FieldTracker(fields=['profile_picture'])

    # Nastavení emailu jako primárního identifikátoru
    USERNAME_FIELD = "email"

    # Pole, která jsou vyžadována při vytváření superuživatele
    REQUIRED_FIELDS = ["username"]

    # Připojení vlastního manažera
    objects = CustomUserManager()


    def __str__(self):
        return self.username


    @property
    def profile_picture_name(self):
        '''
        Definice jména profilového obráku

        :return: Jméno profilového obrázku
        '''

        return f"{slugify(self.email.replace('@', '_').replace('.', '_'))}_upp_300.jpg"


    @property
    def profile_picture_directory(self):
        '''
        Definice jména profilového obráku

        :return: Jméno profilového obrázku
        '''

        return f"images/profile_pictures/users/"

    @property
    def profile_picture_path(self):
        '''
        Definice cesty profilového obráku.

        :return: Cesta profilového obráku.
        '''

        return os.path.join(self.profile_picture_directory, self.profile_picture_name)


    @classmethod
    def default_profile_picture_path(cls):
        # Cesta k defaultnímu obrázku ze složky media
        return 'images/profile_pictures/default.jpg'




    def save(self, *args, **kwargs):
        '''
        Nastavení uživatelského jména a profilového obrázku při založení účtu

        :param args: Poziceové argumenty pro super().save()
        :param kwargs: Klíčové argumenty pro super().save()
        :return: None
        '''

        # Přiřadí uživatelské jméno a profilového obrázku
        if not self.pk:
            self.username = create_username(self.email, CustomUser)
            self.profile_picture = create_profile_picture(
                self.profile_picture_path,
                CustomUser.default_profile_picture_path()
            )

        # Uložení instance
        super().save(*args, **kwargs)




