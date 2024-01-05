from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save, pre_save
from users.models import CustomUser  # Importuj CustomUser z users.models
from django.contrib.auth import get_user_model


class ArticleAuthor(models.Model):
    # Vytvoření vztahu "one-to-one" s modelem CustomUser
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)

    # Obrázek profilového obrázku pro autora článku
    profile_picture = models.ImageField(upload_to="images/profile_pictures/authors/", null=True, blank=True)

    # Ukládá poslední uživatelské jméno před smazáním uživatele
    author = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        # Textová reprezentace instance (pro administrační rozhraní a výpisy)
        return self.author if self.author else "Unknown"

# Signál pro zachování autora článku při smazání uživatele
@receiver(pre_delete, sender=CustomUser)
def delete_user(sender, instance, **kwargs):
    try:
        author = ArticleAuthor.objects.get(user=instance)
        author.user = None
        author.save()
    except ArticleAuthor.DoesNotExist:
        pass

# Signál pro kopírování profilového obrázku uživatele do profilového obrázku autora
@receiver(post_save, sender=CustomUser)
def copy_profile_picture(sender, instance, created, **kwargs):
    if created:
        try:
            author = ArticleAuthor.objects.get(user=instance)
            author.profile_picture = instance.profile_image
            author.author = instance.username
            author.save()
        except ArticleAuthor.DoesNotExist:
            pass

#
# @receiver(pre_save, sender=get_user_model())
# def copy_profile_picture(sender, instance, **kwargs):
#     try:
#         if ArticleAuthor.objects.filter(user=instance).exists():
#             user = get_user_model().objects.get(pk=instance.pk)
#             author = ArticleAuthor.objects.get(user=user)
#             author.profile_picture = user.profile_image
#             author.author = user.username
#             author.save()
#     except ArticleAuthor.DoesNotExist:
#         pass
