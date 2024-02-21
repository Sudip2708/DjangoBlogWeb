from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from model_utils import FieldTracker
import os

from .managers import CustomUserManager
from utilities.for_users.create_default_username import create_default_username
from utilities.for_users.create_default_profile_picture import create_default_profile_picture

from utilities.shared.create_thumbnail import create_thumbnail

class OrderedBooleanField(models.Model):
    """
    Pole boolean s informací o pořadí.
    """
    value = models.BooleanField(default=False)
    order = models.PositiveIntegerField(unique=True)
    hash = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.value)


class CustomUser(AbstractUser):
    '''
    Rozšiřuje Django vestavěný model AbstractUser o pole pro profilové obrázky.

    Nastavuje email jako hlavní identifikátor (namísto username)

    username
    email
    profile_picture
    profile_picture_thumbnail

    [hint]
    profile_picture_tracker
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()
    '''


    # Pole pro uživatelské jméno
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True
    )

    # Pole pro email
    email = models.EmailField(
        _("email_address"),
        unique=True
    )

    # Pole pro profilový obrázek
    profile_picture = models.ImageField(
        _("profile_picture"),
        upload_to="images/profile_pictures/users/"
    )

    # Pole pro miniaturu pro profilový obrázek
    profile_picture_thumbnail = models.ImageField(
        _("profile_picture_thumbnail"),
        upload_to="images/profile_pictures/users/",
        null=True
    )

    # Pole pro id Autora (je-li)
    linked_author_id = models.PositiveIntegerField(null=True, blank=True)


    # FieldTracker pro sledování změn v profile_picture
    profile_picture_tracker = FieldTracker(fields=['profile_picture'])

    # Nastavení emailu jako primárního identifikátoru
    USERNAME_FIELD = "email"

    # Pole, která jsou vyžadována při vytváření superuživatele
    REQUIRED_FIELDS = ["username"]

    # Připojení vlastního manažera
    objects = CustomUserManager()


    # Pole pro sidebar
    sidebar = models.BooleanField(default=True)

    # Pole pro sidebar > tags
    sidebar_search = OrderedBooleanField(value=False, order=1, hash="#search")

    # Pole pro sidebar > user
    sidebar_user = OrderedBooleanField(value=True, order=2, hash="#user")

    # Pole pro sidebar > user > __user_dropdown_menu__.html
    sidebar_user_user_menu = models.BooleanField(default=False)

    # Pole pro sidebar > user > author > __author_dropdown_menu__.html
    sidebar_user_author_menu = models.BooleanField(default=False)

    # Pole pro sidebar > category
    sidebar_category = OrderedBooleanField(value=True, order=3, hash="#category")

    # Pole pro sidebar > category > Zobrazení / Skrytí lišty navigace
    sidebar_category_navigation = models.BooleanField(default=True)

    # Pole pro sidebar > search
    sidebar_tags = OrderedBooleanField(value=True, order=4, hash="#tags")

    def __str__(self):
        return self.username


    @property
    def sidebars(self):
        return [self.sidebar_search, self.sidebar_user, self.sidebar_category, self.sidebar_tags]


    def sidebar_move_up(self, sidebar):
        """
        Posune toto pole nahoru o jedno místo.
        """
        current_sidebar = None
        for i in self.sidebars:
            if sidebar.startswith(i.hash):
                current_sidebar = i
        current_sidebar_position = current_sidebar.order
        previouse_sidebar_position = current_sidebar_position - 1
        previouse_sidebar = None
        for i in self.sidebars:
            if i.order == previouse_sidebar_position:
                previouse_sidebar = i
        previouse_sidebar.order, current_sidebar.order = current_sidebar.order, previouse_sidebar.order
        self.save()


    def sidebar_move_down(self, sidebar):
        """
        Posune toto pole dolu o jedno místo.
        """
        sidebars = [self.sidebar_search, self.sidebar_user, self.sidebar_category, self.sidebar_tags]
        current_sidebar = None
        for i in self.sidebars:
            if sidebar.startswith(i.hash):
                current_sidebar = i
        current_sidebar_position = current_sidebar.order
        next_sidebar_position = current_sidebar_position + 1
        next_sidebar = None
        for i in self.sidebars:
            if i.order == next_sidebar_position:
                next_sidebar = i
        next_sidebar.order, current_sidebar.order = current_sidebar.order, next_sidebar.order
        self.save()



    @property
    def slugify_email(self):
        '''
        Slugifikace emailu

        Všechna znaky malémi písmeny.
        Odstranění z emailové adresy všech znaků, které nejsou vhodné pro použití v URL.
        Nahrazení zavináče a teček podtržítky.

        [hint]
        slugify
        '''
        return f"{slugify(self.email.replace('@', '_').replace('.', '_'))}"


    @property
    def profile_picture_name(self):
        '''
        Definice jména profilového obráku

        Přední část je slagifikovaný email.
        Dodatek tvoří zkrazka pro User Profile Picture (upp) a hodnota velikosti (300).
        '''
        return f"{self.slugify_email}_upp_300.jpg"


    @property
    def profile_picture_thumbnail_name(self):
        '''
        Definice jména miniatury profilového obráku

        Přední část je slagifikovaný email.
        Dodatek tvoří zkrazka pro User Profile Picture a hodnota velikosti.
        '''
        return f"{self.slugify_email}_upp_150.jpg"


    @property
    def profile_picture_directory(self):
        '''
        Cesta k složce pro profilové obrázky z media root

        (složka profile_pictures obsahuje i složku authors pro profilové obrázky autora)
        '''
        return "images/profile_pictures/users/"


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

        # Vytvoření uživatelského jména a profilového obrázku, při založení instance.
        if not self.pk:
            os.makedirs(self.profile_picture_path, exist_ok=True)
            self.username = create_default_username(self.slugify_email, CustomUser)
            self.profile_picture = create_default_profile_picture(self.profile_picture_path)

        # Kontrola, zda byl změněn profilový obrázek.
        change_of_profile_picture = self.profile_picture_tracker.has_changed('profile_picture')

        # Uložení instance
        super().save(*args, **kwargs)

        # Pokud byl změně profilový obrázek, bude změněna i jeho miniatura.
        if change_of_profile_picture:
            create_thumbnail(self)










