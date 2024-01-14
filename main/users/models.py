from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .utils.create_username import create_username
from .utils.create_profile_picture import create_profile_picture
from model_utils import FieldTracker


class CustomUser(AbstractUser):

    # Pole pro uživatelské jméno
    username = models.CharField(max_length=150, unique=True)

    # Pole pro email
    email = models.EmailField(_("email address"), unique=True)

    # Pole pro profilový obrázek
    profile_image = models.ImageField(_("profile image"),
                                      upload_to="images/profile_pictures/users/")

    # FieldTracker pro sledování změn v profile_image
    profile_image_tracker = FieldTracker(fields=['profile_image'])

    # Nastavení emailu jako primárního identifikátoru
    USERNAME_FIELD = "email"

    # Pole, která jsou vyžadována při vytváření superuživatele
    REQUIRED_FIELDS = ["username"]

    # Připojení vlastního manažera
    objects = CustomUserManager()



    def __str__(self):
        return self.username


    @property
    def profile_image_name(self):
        '''
        Definice jména profilového obráku

        :return: Jméno profilového obrázku
        '''
        return f"{slugify(self.email.replace('@', '_').replace('.', '_'))}_upp_300.jpg"

    @property
    def profile_image_directory(self):
        '''
        Definice jména profilového obráku

        :return: Jméno profilového obrázku
        '''
        return f"images/profile_pictures/users/"


    def save(self, *args, **kwargs):
        '''
        Při ukládání instance CustomUser provede nastavení uživatelského jména a profilového obrázku, pokud neexistuje ID (primární klíč).

        :param args: Poziceové argumenty pro super().save()
        :param kwargs: Klíčové argumenty pro super().save()
        :return: None
        '''

        # Přiřadí uživatelské jméno a profilového obrázku
        if not self.pk:
            self.username = create_username(self.email, CustomUser)
            self.profile_image = create_profile_picture(self.profile_image_directory, self.profile_image_name)

        # Uložení instance
        super().save(*args, **kwargs)




