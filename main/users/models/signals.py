from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from users.models.user_profile_model import UserProfile


# Vytvoření instance UserProfile připojené k nově vytvořenému uživatelskému účtu
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
