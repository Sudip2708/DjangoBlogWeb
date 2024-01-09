from django.db import models
from users.models import CustomUser

class ArticleAuthor(models.Model):

    # Vztah "one-to-one" s modelem CustomUser (po smazání uživatel autor zůstává)
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    # Obrázek profilového obrázku pro autora článku
    author_profile_picture = models.ImageField(upload_to="images/profile_pictures/authors/")

    # Ukládá poslední uživatelské jméno před smazáním uživatele
    author = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.author

    def save(self, *args, **kwargs):
        # Nastaví author a profile_picture podle CustomUser při vytváření ArticleAuthor
        if not self.pk:
            self.author = self.user.username
            self.profile_picture = self.user.profile_image

        super().save(*args, **kwargs)
