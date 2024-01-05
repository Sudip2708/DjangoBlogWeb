from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    # Zachování pole pro username
    username = models.CharField(max_length=150, unique=True)

    # Nově přidané pole pro email
    email = models.EmailField(_("email address"), unique=True)

    # Nově přidané pole pro profilový obrázek
    profile_image = models.ImageField(_("profile image"), upload_to="images/profile_pictures/users/", default="images/profile_pictures/users/default.jpg")

    # Nastavení emailu jako primárního identifikátoru
    USERNAME_FIELD = "email"

    # Nastavení emailu jako primárního identifikátoru
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    @staticmethod
    @receiver(pre_save, sender="users.CustomUser")
    def create_username_from_email(sender, instance, **kwargs):
        '''
        Tato metoda se spustí před každým uložením instance CustomUser.

        :param sender: Třída nebo model, který posílá signál (v tomto případě CustomUser).
        :param instance: Instance CustomUser, která bude uložena.
        :param kwargs: Dodatečné argumenty, které mohou být předány spouštějícím mechanismem signálu.

        :return: Pokud uživatel nemá nastavené username, metoda ho vygeneruje z přední části e-mailu.
                Pokud se již username vyskytuje, přidá pořadové číslo.

    '''
        if not instance.username:

            # Vytvoření základu pro username: Přední část emailu (před @) + převést velká písmena na malá
            username = instance.email.split('@')[0].lower()

            # Přidat pořadové číslo v případě, že username již existuje
            counter = 1
            new_username = username
            while CustomUser.objects.filter(username=new_username).exists():
                counter += 1
                new_username = f"{username}_{counter}"

            instance.username = new_username