from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import (pre_save,
                                      post_save)

from ..models.custom_user import CustomUser
from .user_handlers import (default_values_handler,
                            profile_picture_handler)


# Checking and updating default values when the user logs in
@receiver(user_logged_in, sender=CustomUser)
def handle_user_logged_in(sender, request, user, **kwargs):
    user.check_default_values()


# Processing default values
@receiver(pre_save, sender=CustomUser)
def handle_title_slug(sender, instance, **kwargs):
    default_values_handler.handle_default_values_pre_save(instance)


# Processing the profile picture
@receiver(post_save, sender=CustomUser)
async def handle_picture_post_save(sender, instance, **kwargs):
    await profile_picture_handler.handle_picture_post_save(instance)
