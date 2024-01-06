from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):

    # Pole pro uživatelské jméno
    username = models.CharField(max_length=150, unique=True)

    # Pole pro email
    email = models.EmailField(_("email address"), unique=True)

    # Pole pro profilový obrázek
    profile_image = models.ImageField(_("profile image"),
                                      upload_to="images/profile_pictures/users/",
                                      default="images/profile_pictures/users/default.jpg")

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
