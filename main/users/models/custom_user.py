from django.contrib.auth.models import AbstractUser
from django.db import models

from .custom_user_data.managers import CustomUserManager
from .custom_user_data.mixin_settings import UserSettingsMixin
from .custom_user_data.profile_picture_processing import profile_picture_processing


class CustomUser(AbstractUser, UserSettingsMixin):
    '''
    Třída definující nastavení polí pro přihlášeného uživatele.

    Třída dědí z tříd:
    - AbstractUser: Třída poskytující implementaci běžných funkcí pro správu uživatelského účtu.
    - UserSettingsMixin: Třída pro oddělení obsahu pro správu a nastavení postranních panelů.

    Třída vytváří nebo přepisuje tyto pole:
    - email: Email uživatele.
    - username: Jméno zvolené uživatelem.
    - username_slug: Slug pro jméno zvolené uživatelem (pro URL).
    - profile_picture: Profilový obrázek uživatele.
    - profile_picture_thumbnail: Miniatura profilového obrázku.

    Z mixinu UserSettingsMixin třída dědí tato pole:
    - sidebar_settings: Pole pro slovník s daty pro nastavení vzhledu bočního panelu.
    - sidebar_order: Pole pro slovník s daty pro nastavení pořadí bočních panelů.
    - settings: Pole pro slovník s daty pro další dodatečná nastavení.

    Z třídy AbstractUser dědí ještě i tato pole:
    - id: Identifikační číslo uživatele.
    - password: Heslo uživatele.
    - first_name: Jméno uživatele.
    - last_name: Příjmení uživatele.
    - date_joined: Datum registrace.
    - last_login: Datum posledního přihlášení.
    - is_superuser: Nastavení, jestli je uživatel i superuživatel.
    - is_staff: Nastavení, jestli je uživatel ve skupině staff.
    - is_active: Nastavení, jestli je uživatel přihlášen.
    - groups: Nastavení skupin, do kterých uživatel patří.
    - user_permissions: Nastavení uživatelových práv.

    Třída definuje tyto atributy pro profilové obrázky:
    - default_picture: Cesta z Media k defaultnímu obrázku (použit při vytvoření instance bez udání obrázku).
    - upload_path: Cesta z Media pro uložení všech velikostních variant hlavního obrázku.
    - new_picture: Boolean hodnota, zda došlo k novému nahrání obrázku (nastavuje se ve formuláři po obdržení
                   nového souboru pro obrázek a je zachytávána v post_save signálu pro zpracování obrázku).

    Třída dále nastavuje atribut:
    - USERNAME_FIELD: Definice pole, které se má použít jako primární identifikátor pro přihlášení (zde 'email').
    - REQUIRED_FIELDS: Přepsání defaultní hodnoty ('email') hodnotou pro 'username' pro vyřešení konfliktu s migrací.

    A přes 'objects' nastavuje vlastního manažera,
    který se má použít pro změnu nastavení identifikace uživatele
    a superuživatele (z uživatelského jména na email).

    Metody definované v této části modelu:
    - __str__: Získání textové reprezentace modelu (dle hodnoty pole pro jméno autora).
    - profile_picture_processing: Metoda pro úpravu profilového obrázku.

    Metody definované v UserSettingsMixin:
    - get_sorted_sidebar_panels: Metoda vrací data pro vykreslení postranních panelů v nastaveném pořadí.
    - change_sidebar_bool_value: Metoda pro změnu boolean hodnot pro nastavení bočního panelu.
    - change_sidebar_order_value: Metoda pro změnu pořadí bočních panelů.
    - change_settings_bool_value: Metoda pro změnu boolean hodnot pro dodatečná nastavení uživatele.
    '''

    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )

    username = models.CharField(
        verbose_name='User Name',
        blank=True,
        unique=True,
        max_length=50,
    )

    slug = models.SlugField(
        verbose_name='Username Slug',
        blank=True,
        unique=True,
    )

    default_picture = 'images/profile_pictures/default.jpg'
    upload_path = 'images/profile_pictures/users/'
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username_slug

    def profile_picture_processing(self):
        ''' Metoda pro úpravu profilového obrázku (a vytvoření miniatury). '''
        return profile_picture_processing(self)
