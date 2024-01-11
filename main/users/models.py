from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from model_utils import FieldTracker
import os
from shutil import copyfile
from django.utils.text import slugify

class CustomUser(AbstractUser):

    # Pole pro uživatelské jméno
    username = models.CharField(max_length=150, unique=True)

    # Pole pro email
    email = models.EmailField(_("email address"), unique=True)

    # Pole pro profilový obrázek
    profile_image = models.ImageField(_("profile image"),
                                      upload_to="images/profile_pictures/users/")

    # FieldTracker pro sledování změn v profile_image
    tracker = FieldTracker(fields=['profile_image'])

    # Nastavení emailu jako primárního identifikátoru
    USERNAME_FIELD = "email"

    # Pole, která jsou vyžadována při vytváření superuživatele
    REQUIRED_FIELDS = ["username"]

    # Připojení vlastního manažera
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        # Pokud uživatel nemá nastavené uživatelské jméno (při vytvoření nové instance)
        if not self.username:

            # Vytvoření základu pro uživatelské jméno: Přední část emailu (před @) + převést velká písmena na malá
            username = self.email.split('@')[0].lower()

            # Přidání pořadového čísla v případě, že uživatelské jméno již existuje
            counter = 1
            new_username = username
            while CustomUser.objects.filter(username=new_username).exists():
                counter += 1
                new_username = f"{username}_{counter}"
            self.username = new_username




        if not self.profile_image:

            # Cesta k defaultnímu obrázku
            default_image_path = 'images/profile_pictures/default.jpg'

            # Název souboru pro nový obrázek
            new_image_name = f"{slugify(self.email)}_pp_300.jpg"
            new_image_path = f"images/profile_pictures/users/{new_image_name}"

            # Úplná cesta k souboru defaultního obrázku
            default_image_full_path = os.path.join(settings.MEDIA_ROOT, default_image_path)

            # Úplná cesta k novému souboru
            new_image_full_path = os.path.join(settings.MEDIA_ROOT, new_image_path)

            # Kopírování defaultního obrázku na nové místo
            copyfile(default_image_full_path, new_image_full_path)

            # Přidání vytvořeného souboru do pole profile_image
            self.profile_image.name = new_image_path

        super().save(*args, **kwargs)

    @property
    def is_author(self):
        try:
            # Zkusí najít záznam v ArticleAuthor, kde uživatel je aktuální uživatel
            author_instance = ArticleAuthor.objects.get(user=self)
            return author_instance
        except ArticleAuthor.DoesNotExist:
            # Pokud ArticleAuthor s tímto uživatelem neexistuje, vrátí None
            return None
