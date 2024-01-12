from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from model_utils import FieldTracker


class ArticleAuthor(models.Model):

    # Vztah "one-to-one" s modelem CustomUser (po smazání uživatel autor zůstává)
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    # Obrázek profilového obrázku pro autora článku
    author_profile_picture = models.ImageField(upload_to="images/profile_pictures/authors/")

    # Ukládá poslední uživatelské jméno před smazáním uživatele
    author = models.CharField(max_length=150, unique=True)

    # FieldTracker pro sledování změn v profile_image
    tracker = FieldTracker(fields=['author_profile_picture'])


    def __str__(self):
        return self.author




    def save(self, *args, **kwargs):
        # Nastaví author a profile_picture podle CustomUser při vytváření ArticleAuthor
        if not self.pk:
            self.author = self.user.username
            self.profile_picture = f"{slugify(self.user.email.replace('@', '_').replace('.', '_'))}_app_300.jpg"

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
