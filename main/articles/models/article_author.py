from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker
import os


class ArticleAuthor(models.Model):

    # Vztah "one-to-one" s modelem CustomUser (po smazání uživatel autor zůstává)
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    # Profilový obrázek autora článku
    profile_picture = models.ImageField(_("author profile picture"), upload_to="images/profile_pictures/authors/")

    # Uživatelské jméno autora článku
    author = models.CharField(_("author"), max_length=150, unique=True)

    # FieldTracker pro sledování změn v profile_picture
    profile_picture_tracker = FieldTracker(fields=['profile_picture'])


    def __str__(self):
        return self.author


    @property
    def profile_picture_name(self):
        '''
        Definice jména profilového obráku

        :return: Jméno profilového obrázku autora
        '''

        return f"{slugify(self.user.email.replace('@', '_').replace('.', '_'))}_app_300.jpg"


    @property
    def profile_picture_directory(self):
        '''
        Definice cesty k profilovému obráku

        :return: Cesta k profilovému obrázku
        '''

        return f"images/profile_pictures/authors/"

    @property
    def profile_picture_path(self):
        '''
        Definice umístění a jména profilového obráku.

        :return: Tuple umístění a jména profilového obráku.
        '''

        return os.path.join(self.profile_picture_directory, self.profile_picture_name)


    def save(self, *args, **kwargs):
        # Nastaví author a profile_picture podle CustomUser při vytváření ArticleAuthor
        if not self.pk:
            self.author = self.user.username
            self.profile_picture = self.user.profile_picture
            self.profile_picture.name = self.profile_picture_name

        super().save(*args, **kwargs)


    @classmethod
    def user_is_author(cls, user):
        '''
        Třídní metoda pro zjištění, zda je určitý uživatel i autorem

        :param user: Instance uživatele
        :return: True / False
        '''

        try:
            ArticleAuthor.objects.get(user=user)
            return True

        except ArticleAuthor.DoesNotExist:
            return False
